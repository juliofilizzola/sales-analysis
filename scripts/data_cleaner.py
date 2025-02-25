def cleaner(df):
    # Drop rows with missing values
    df = df.dropna()
    # Drop duplicates
    df['data'] = df['data'].drop_duplicates()
    df['total_sale'] = df['quantity'] * df['price']
    return df
