
import pandas as pd


def load_data(path="data\raw\creditcard.csv")-> pd.DataFrame:
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