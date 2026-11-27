
import pandas as pd


def load_data(path: str = 'data/raw/creditcard.csv')-> pd.DataFrame:
    """
    Load data from a given file path.

    Args:
        path (str): The file path to load data from.

    Returns:
        data: The loaded data.
    """
    
    print(f"Loading data from {path}...")
    df = pd.read_csv(path)
    return df


def clean_data(df: pd.DataFrame)-> pd.DataFrame:
    """
    Clean the data by removing duplicates.

    Args:
        df (pd.DataFrame): The input DataFrame to clean."""
    clean_df = df.drop_duplicates().reset_index(drop=True)    
    print(f'Duplicates Dropped : {df.shape[0] - clean_df.shape[0]}')

    return clean_df