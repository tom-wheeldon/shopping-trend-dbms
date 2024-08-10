import pandas as pd
import matplotlib.pyplot as plt
from db_connection import get_db_connection

def visualise_customer_demographics():
    conn = get_db_connection()
    query = "SELECT * FROM CustomerDemographicView"
    df = pd.read_sql(query, conn)

    grouped = df.groupby(['Location', 'Gender']).sum().reset_index()

    plt.figure(figsize=(12, 6))
    for gender in grouped['Gender'].unique():
        subset = grouped[grouped['Gender'] == gender]
        plt.bar(subset['Location'], subset['NumCustomers'], label=gender)

    plt.title('Customer Demographics by Location and Gender')
    plt.xlabel('Location')
    plt.ylabel('Number of Customers')
    plt.legend(title='Gender')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig('customer_demographics.png')
    plt.show()
    conn.close()
