import pandas as pd
from typing import Dict, Any


@data_loader
def main(**kwargs) -> pd.DataFrame:
    # Sample monster weakness data with true labels and model predictions
    data = {
        'monster_id': range(1, 11),
        'true_weakness': ['fire', 'water', 'wind', 'fire', 'water', 
                         'wind', 'fire', 'water', 'wind', 'fire'],
        'predicted_weakness': ['fire', 'water', 'fire', 'fire', 'water',
                             'water', 'fire', 'wind', 'wind', 'water']
    }
    
    return pd.DataFrame(data)