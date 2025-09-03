if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd
from typing import List, Dict

@transformer
def transform_data(data: pd.DataFrame, *args, **kwargs) -> List[pd.DataFrame]:
    """
    Transforms each chunk by adding 'risk_score_2' based on 'cardiac_risk_score'.
    """
    data = data.copy()

    # Sum up risk factors to get cardiac risk score
    data['cardiac_risk_score'] = (
        data['age_score'].fillna(0) +
        data['bp_score'].fillna(0) +
        data['pulse_score'].fillna(0) +
        data['bmi_score'].fillna(0)
    )

    # Risk interpretation: higher score = higher risk
    def assign_risk_category(score: int) -> str:
        if score <= 1:
            return 'Low risk'
        elif 2 <= score <= 3:
            return 'Medium risk'
        elif score >= 4:
            return 'High risk'
        return 'Unknown'

    data['serious_event_risk'] = data['cardiac_risk_score'].apply(assign_risk_category)
    return data