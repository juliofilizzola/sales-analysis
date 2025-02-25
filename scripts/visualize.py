import matplotlib.pyplot as plt


def visualize(data, path_data):
        """
        Generates graphs from the data.
        :param data: DataFrame with the cleaned data.
        :param path_data: Path to save the graphs.
        """
        # Sales by day graph
        sales_by_day = data.groupby('data')['total_sale'].sum()
        sales_by_day.plot(kind='bar', title='Sales by Day')
        plt.savefig(f"{path_data}/sales_by_day.png")
        plt.close()

        # Sales by city graph
        sales_by_city = data.groupby('city')['total_sale'].sum()
        sales_by_city.plot(kind='pie', autopct='%1.1f%%', title='Sales by City')
        plt.savefig(f"{path_data}/sales_by_city.png")
        plt.close()
