import pandas as pd
import matplotlib.pyplot as plt
from db_connection import get_db_connection

def visualise_top_10_products():
    conn = get_db_connection()
    query = "SELECT * FROM Top10ProductsView"
    df = pd.read_sql(query, conn)

    plt.figure(figsize=(10, 6))
    plt.barh(df['ItemPurchased'], df['TotalSales'], color='skyblue')

    plt.title('Top 10 Products by Sales')
    plt.xlabel('Total Sales')
    plt.ylabel('Product')
    plt.tight_layout()

    plt.savefig('top_10_products.png')
    plt.show()
    conn.close()
