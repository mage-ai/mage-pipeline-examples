import numpy as np
from typing import Dict


@custom
def main(confusion_matrix_: Dict[str, np.ndarray], **kwargs) -> Dict[str, float]:
    # Extract confusion matrix and elements
    confusion_matrix = confusion_matrix_['confusion_matrix']
    elements = confusion_matrix_['elements']
    
    # Calculate recall for each element
    recalls = {}
    for i, element in enumerate(elements):
        # True positives for this element
        true_positives = confusion_matrix[i, i]
        
        # Total actual occurrences for this element (row sum)
        total_actuals = np.sum(confusion_matrix[i, :])
        
        # Calculate recall, handling division by zero
        if total_actuals == 0:
            recall = 0.0
        else:
            recall = true_positives / total_actuals
            
        recalls[f'{element}_recall'] = recall
        
    return recalls