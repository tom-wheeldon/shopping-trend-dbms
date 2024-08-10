import pandas as pd
import matplotlib.pyplot as plt
from db_connection import get_db_connection

def visualise_seasonal_sales_trends():
    conn = get_db_connection()
    query = "SELECT * FROM SeasonalSalesTrendsView"
    df = pd.read_sql(query, conn)

    plt.figure(figsize=(10, 5))
    plt.plot(df['Season'], df['TotalSales'], marker='o')

    plt.title('Seasonal Sales Trends')
    plt.xlabel('Season')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.tight_layout()

    plt.savefig('seasonal_sales_trends.png')
    plt.show()
    conn.close()
