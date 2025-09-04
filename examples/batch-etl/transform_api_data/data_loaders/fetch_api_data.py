import io
import requests

import pandas as pd


@data_loader
def load_data_from_api(*args, **kwargs):
    url = 'https://raw.githubusercontent.com/mage-ai/datasets/refs/heads/master/medical.csv'
    response = requests.get(url)

    return pd.read_csv(io.StringIO(response.text), sep=',')