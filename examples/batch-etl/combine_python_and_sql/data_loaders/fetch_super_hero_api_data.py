from typing import Any, Dict, List

import pandas as pd
import requests


@data_loader
def get_heroes(**kwargs: Any) -> pd.DataFrame:
    """
    Fetches superheroes

    Args:
        **kwargs: Arbitrary keyword arguments

    Returns:
        pd.DataFrame: Pandas DataFrame containing hero data
    """
    response = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')
    response.raise_for_status() 

    return pd.DataFrame(response.json())