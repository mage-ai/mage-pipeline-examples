from io import StringIO
import pandas as pd
import requests

DEFAULT_CSV_URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

@data_loader
def fetch_csv_from_url(*args, **kwargs):
    """
    Download a CSV file from the specified URL and load it into a pandas DataFrame.
    This function does not perform any cleaning; it only loads raw data for downstream processing.

    Args:
        url (str): The URL of the CSV file to download.
        **kwargs: Additional keyword arguments to pass to pandas.read_csv if needed.

    Returns:
        pd.DataFrame: DataFrame containing the raw CSV data.
    """

    # Send a GET request to fetch the CSV content
    url: str = kwargs.get('url') or DEFAULT_CSV_URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Read the CSV content into a pandas DataFrame
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data)

    return df
