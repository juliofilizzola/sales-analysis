def calculate_metric(data):
    metric = {
        'total_sales': data['total_sale'].sum(),
        'average_sales_per_day': data.groupby('data')['total_sale'].sum().mean(),
        'most_sold_product': data['product'].value_counts().idxmax(),
        'city_with_highest_sales': data.groupby('city')['total_sale'].sum().idxmax()
    }
    return metric
