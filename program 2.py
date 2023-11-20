import pandas as pd


data = {
    'customer_id': [1, 2, 1, 3, 2, 3],
    'order_date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-03', '2023-01-02', '2023-01-04'],
    'product_name': ['Product_A', 'Product_B', 'Product_A', 'Product_C', 'Product_B', 'Product_C'],
    'order_quantity': [5, 8, 3, 2, 7, 4]
}

order_data = pd.DataFrame(data)


total_orders_per_customer = order_data.groupby('customer_id').size()
print("Total Orders Per Customer:")
print(total_orders_per_customer)
print("\n")


average_order_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()
print("Average Order Quantity Per Product:")
print(average_order_quantity_per_product)
print("\n")


earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()
print("Earliest Order Date:", earliest_order_date)
print("Latest Order Date:", latest_order_date)
