import io
import requests

import pandas as pd


@data_loader
def load_data_from_api(**kwargs) -> pd.DataFrame:
    """
    Template for loading data from API
    """
    url = 'https://raw.githubusercontent.com/mage-ai/datasets/master/titanic_survival.csv'

    response = requests.get(url)
    return pd.read_csv(io.StringIO(response.text), sep=',')



@test
def test_rows(df) -> None:
    assert len(df.index) >= 891 is not None, 'The data doesn’t have enough rows'


@test
def test_columns(df) -> None:
    assert len(df.columns) >= 12 is not None, 'The data doesn’t have enough columns'
