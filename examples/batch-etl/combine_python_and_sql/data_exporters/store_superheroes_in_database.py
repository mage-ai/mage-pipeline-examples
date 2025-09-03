import os
from os import path

from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.duckdb import DuckDB
from pandas import DataFrame


@data_exporter
def export_data_to_duckdb(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to DuckDB database.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#duckdb
    """

    # Get arguments from kwargs with defaults
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    table_name = kwargs.get('table_name', 'superheroes')
    database_path = os.path.join(get_repo_path(), kwargs.get('database_path', 'examples.db'))

    # Create SQLite connection and write DataFrame
    with DuckDB.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            df,
            None,
            table_name=table_name,
            index=False,  # Specifies whether to include index in exported table
            if_exists='replace',  # Specify resolution policy if table name already exists
        )

    return df.head(5)