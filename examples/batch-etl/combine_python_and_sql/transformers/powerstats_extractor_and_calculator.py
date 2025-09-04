from typing import Union
from ast import literal_eval

import pandas as pd


@transformer
def extract_powerstats_and_add_statistics(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Extracts powerstats values from a DataFrame column and adds statistical columns.
    Keeps original data and adds aggregates for each power stat.
    """
    powerstats_col = kwargs.get('powerstats_col', 'powerstats')
    
    if powerstats_col not in df.columns:
        raise KeyError(f"Column '{powerstats_col}' not found in DataFrame")
    
    # Define stat columns we want to extract
    stat_cols = ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']
    
    def parse_powerstats(val: Union[str, dict]) -> dict:
        if isinstance(val, dict):
            return {col: val.get(col, None) for col in stat_cols}
            
        if isinstance(val, str):
            try:
                parsed = literal_eval(val)
                return {col: parsed.get(col, None) for col in stat_cols}
            except:
                return {col: None for col in stat_cols}
                
        return {col: None for col in stat_cols}
    
    # Extract powerstats into separate columns
    powerstats_df = pd.DataFrame([parse_powerstats(x) for x in df[powerstats_col]])
    
    # Add powerstats columns to original df
    result_df = pd.concat([df, powerstats_df], axis=1)
    
    # Convert stat columns to numeric
    for col in stat_cols:
        result_df[col] = pd.to_numeric(result_df[col], errors='coerce')
        
        # Calculate statistics for this stat column
        result_df[f'{col}_mean'] = result_df[col].mean()
        result_df[f'{col}_max'] = result_df[col].max()
        result_df[f'{col}_min'] = result_df[col].min()
        result_df[f'{col}_median'] = result_df[col].median()
    
    return result_df