import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

LABEL_COLUMN = 'Survived'


@transformer
def transform_df(df: pd.DataFrame, *args) -> pd.DataFrame:
    """Transform DataFrame using SimpleImputer for numeric columns"""
    # Select only the numeric columns we want to process
    df = df[['Age', 'Fare', 'Parch', 'Pclass', 'SibSp', 'Survived']]
    df_features = df.drop(columns=[LABEL_COLUMN])
    
    # Create and fit the imputer
    imputer = SimpleImputer(strategy='median', missing_values=np.nan)
    
    # Transform the data
    imputed_array = imputer.fit_transform(df_features)
    
    # Convert back to DataFrame with original column names
    transformed_df = pd.DataFrame(imputed_array, columns=df_features.columns, index=df_features.index)
    transformed_df[LABEL_COLUMN] = df[LABEL_COLUMN]
    
    return [transformed_df, imputer]