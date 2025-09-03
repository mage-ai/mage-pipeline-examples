import numpy as np
from typing import Dict, Any, Tuple


@data_exporter
def main(arg1: Any, arg2: Any, arg3: Any, arg4: Any, **kwargs) -> Dict[str, Any]:
    accuracy = arg1
    precisions = arg2
    recalls = arg3
    baseline = arg4
    
    # Compare model performance against baseline
    model_evaluation = {
        'model_accuracy': accuracy,
        'baseline_score': baseline,
        'improvement_over_baseline': accuracy - baseline
    }

    # Add precision and recall metrics
    model_evaluation.update(precisions)
    model_evaluation.update(recalls)

    # Calculate F1 scores for each element
    elements = ['fire', 'water', 'wind']
    for element in elements:
        precision = precisions[f'{element}_precision']
        recall = recalls[f'{element}_recall']
        
        if precision + recall == 0:
            f1 = 0.0
        else:
            f1 = 2 * (precision * recall) / (precision + recall)
            
        model_evaluation[f'{element}_f1'] = f1

    # Add metric prioritization scenarios
    model_evaluation['scenarios'] = {
        'balanced': accuracy,
        'precision_focused': np.mean(list(precisions.values())),
        'recall_focused': np.mean(list(recalls.values()))
    }

    return model_evaluation