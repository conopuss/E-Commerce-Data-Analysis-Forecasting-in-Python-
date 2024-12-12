import pandas as pd
from data_cleaning import clean_data
from data_manipulation import yearly_sales, monthly_sales, daily_sales, customer_spending, sales_by_category
from data_forecasting import forecast_sales, top_selling_products

def automate_analysis():
    print("Veri okunuyor ve temizleniyor...")
    sales, feedback, products = clean_data()

    print("Veri analizi yapılıyor...")

    # Generate summaries
    yearly_sales_summary = yearly_sales(sales)
    monthly_sales_summary = monthly_sales(sales)
    daily_sales_summary = daily_sales(sales)

    # Customer spending
    sales_with_spending = customer_spending(sales)

    # Product sales by category
    product_sales_summary = sales_by_category(sales, products)

    # Sales forecast
    print("Satış öngörüsü yapılıyor...")
    future_sales_forecast = forecast_sales(monthly_sales_summary)

    # Top selling products
    print("En çok satan ürünler belirleniyor...")
    top_products = top_selling_products(sales, products)

    # Save all reports into an Excel file
    print("Raporlar 'sales_summary.xlsx' dosyasına kaydediliyor...")
    with pd.ExcelWriter('sales_summary.xlsx') as writer:
        yearly_sales_summary.to_excel(writer, sheet_name='Yearly Sales', index=False)
        monthly_sales_summary.to_excel(writer, sheet_name='Monthly Sales', index=False)
        daily_sales_summary.to_excel(writer, sheet_name='Daily Sales', index=False)
        product_sales_summary.to_excel(writer, sheet_name='Product Sales by Category', index=False)
        future_sales_forecast.to_excel(writer, sheet_name='Future Sales Forecast', index=False)
        top_products.to_excel(writer, sheet_name='Top Selling Products', index=False)

    print("Raporlar 'sales_summary.xlsx' dosyasına kaydedildi.")

if __name__ == '__main__':
    automate_analysis()
