import pandas as pd


@transformer
def clean_data(data: pd.DataFrame, *args, **kwargs):
    """
    Cleans the input DataFrame by removing rows with nulls, standardizing text fields,
    converting numeric columns to appropriate types, and dropping duplicates.

    Args:
        data (pd.DataFrame): Raw input DataFrame from upstream fetch block.
        **kwargs (Any): Additional keyword arguments.

    Returns:
        pd.DataFrame: Cleaned DataFrame ready for loading into BigQuery.
    """

    # Remove rows with nulls in all columns
    data_cleaned = data.dropna(how="any")

    # Standardize text fields: strip whitespace and convert to lowercase
    for column in data_cleaned.select_dtypes(include=["object"]).columns:
        data_cleaned[column] = data_cleaned[column].astype(str).str.strip().str.lower()

    # Attempt to convert numeric columns to appropriate types
    for column in data_cleaned.columns:
        # Check if column can be converted to numeric
        try:
            data_cleaned[column] = pd.to_numeric(data_cleaned[column])
        except (ValueError, TypeError):
            # If conversion fails, keep original
            pass

    # Drop duplicate rows
    data_cleaned = data_cleaned.drop_duplicates()

    # Preserve original dtypes for non-object columns
    for column in data.columns:
        if column in data_cleaned.columns:
            data_cleaned[column] = data_cleaned[column].astype(data[column].dtype)

    return data_cleaned
