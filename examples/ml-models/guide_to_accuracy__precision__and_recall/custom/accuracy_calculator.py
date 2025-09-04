import numpy as np
from typing import Dict, Any


@custom
def main(confusion_matrix_: Dict[str, np.ndarray], **kwargs) -> float:
    # Extract confusion matrix
    confusion_matrix = confusion_matrix_['confusion_matrix']
    
    # Calculate accuracy by summing diagonal elements and dividing by total
    accuracy = np.trace(confusion_matrix) / np.sum(confusion_matrix)
    
    return accuracy