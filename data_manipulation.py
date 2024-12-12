import pandas as pd
from data_cleaning import clean_data

# Call clean_data to get the necessary data
sales, feedback, products = clean_data()

def yearly_sales(sales):
    sales['year'] = sales['sales_date'].dt.year
    return sales.groupby('year').agg({
        'quantity': 'sum',
        'price_per_unit': 'sum'
    }).reset_index()

def monthly_sales(sales):
    sales['month'] = sales['sales_date'].dt.month
    return sales.groupby(['year', 'month']).agg({
        'quantity': 'sum',
        'price_per_unit': 'sum'
    }).reset_index()

def daily_sales(sales):
    sales['day'] = sales['sales_date'].dt.day
    return sales.groupby(['year', 'month', 'day']).agg({
        'quantity': 'sum',
        'price_per_unit': 'sum'
    }).reset_index()

def customer_spending(sales):
    customer_spending = sales.groupby('customer_id')['price_per_unit'].sum().reset_index()
    customer_spending.rename(columns={'price_per_unit': 'total_spent'}, inplace=True)
    return sales.merge(customer_spending, on='customer_id', how='left')

def sales_by_category(sales, products):
    merged_data = sales.merge(products[['product_id', 'category']], on='product_id', how='left')
    return merged_data.groupby('category').agg(
        total_quantity=('quantity', 'sum'),
        total_revenue=('price_per_unit', 'sum')
    ).reset_index()

# Save analysis results as CSVs
if __name__ == '__main__':
    yearly = yearly_sales(sales)
    monthly = monthly_sales(sales)
    daily = daily_sales(sales)
    spending = customer_spending(sales)
    category_sales = sales_by_category(sales, products)

    yearly.to_csv('yearly_sales_summary.csv', index=False)
    monthly.to_csv('monthly_sales_summary.csv', index=False)
    daily.to_csv('daily_sales_summary.csv', index=False)
    spending.to_csv('sales_with_spending.csv', index=False)
    category_sales.to_csv('product_sales_summary.csv', index=False)
    print("Data analysis complete and saved.")
