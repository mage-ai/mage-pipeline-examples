import numpy as np
import pandas as pd
from typing import Dict, Any

@custom
def main(data: pd.DataFrame, **kwargs) -> float:
    # Get mode (most common) weakness
    mode_weakness = data['true_weakness'].mode().iloc[0]
    
    # Count occurrences of mode weakness
    mode_count = (data['true_weakness'] == mode_weakness).sum()
    
    # Calculate baseline score
    total_samples = len(data)
    baseline_score = mode_count / total_samples
    
    return baseline_score