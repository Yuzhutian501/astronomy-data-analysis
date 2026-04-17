def normalize_flux(df):
    df['flux'] = (df['flux'] - df['flux'].mean()) / df['flux'].std()
    return df
