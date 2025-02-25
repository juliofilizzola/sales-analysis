import pandas as pd


def data_load(path_file):
    try:
        data = pd.read_csv(path_file)
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None
