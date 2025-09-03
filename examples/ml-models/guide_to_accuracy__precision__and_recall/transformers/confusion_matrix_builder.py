import numpy as np
import pandas as pd
from typing import Dict, Any

@transformer
def main(data: pd.DataFrame, **kwargs) -> Dict[str, np.ndarray]:  # Correct function signature
    # Get unique elements
    elements = sorted(list(set(data['true_weakness'].unique()) |
                         set(data['predicted_weakness'].unique())))
    
    # Initialize confusion matrix
    n = len(elements)
    confusion_matrix = np.zeros((n, n))  # Correct numpy zeros initialization
    
    # Create element to index mapping
    element_to_idx = {element: idx for idx, element in enumerate(elements)}
    
    # Fill confusion matrix
    for true, pred in zip(data['true_weakness'], data['predicted_weakness']):
        true_idx = element_to_idx[true]
        pred_idx = element_to_idx[pred]
        confusion_matrix[true_idx, pred_idx] += 1
        
    return {
        'confusion_matrix': confusion_matrix,
        'elements': np.array(elements)
    }