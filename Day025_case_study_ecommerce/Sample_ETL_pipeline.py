import pandas as pd

# Sample ETL pipeline: Load data from CSV, transform, and output aggregated report

# Load data
customers = pd.read_csv('customers.csv')
orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')
payments = pd.read_csv('payments.csv')

# Join orders with customers and products
data = orders.merge(customers, on='CustomerID') \
             .merge(products, on='ProductID')

# Calculate total spent by each customer
report = data.groupby('Name')['Amount'].sum().reset_index()

print("Customer Spending Report")
print(report)
