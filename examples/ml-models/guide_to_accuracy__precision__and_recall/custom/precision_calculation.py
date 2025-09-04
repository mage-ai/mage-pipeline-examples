import numpy as np
from typing import Dict, Any


@custom
def main(confusion_matrix_: Dict[str, np.ndarray], **kwargs) -> Dict[str, float]:
    # Extract confusion matrix and elements
    confusion_matrix_data = confusion_matrix_
    confusion_matrix = confusion_matrix_data['confusion_matrix']
    elements = confusion_matrix_data['elements']
    
    # Calculate precision for each element
    precisions = {}
    for i, element in enumerate(elements):
        # True positives for this element
        true_positives = confusion_matrix[i, i]
        
        # Total predictions for this element (column sum)
        total_predictions = np.sum(confusion_matrix[:, i])
        
        # Calculate precision, handling division by zero
        precision = 0.0 if total_predictions == 0 else true_positives / total_predictions
        
        precisions[f'{element}_precision'] = precision
        
    return precisions