import pandas as pd

def load_lightcurve(path):
    return pd.read_csv(path)
