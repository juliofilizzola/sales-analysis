def cleaner(df):
    # Drop rows with missing values
    df = df.dropna()
    # Drop duplicates
    df['data'] = df['data'].drop_duplicates()
    df['amount'] = df['quantity'] * df['price']
    return df
