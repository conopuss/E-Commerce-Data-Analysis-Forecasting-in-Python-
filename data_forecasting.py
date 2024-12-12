import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime


def forecast_sales(monthly_sales):
    """
    Predict sales for the next 6 months based on past monthly sales data.
    """
    # Prepare data for regression
    #Bir time kolonu oluşturuyor ve bu kolon "0" dan başlıyor bu sayede "1" den başlayan ay kolonunu çevirmiş oluyor
    #np yani numphy kütüphanesi arange ile bir array oluşturuyor
    monthly_sales['time'] = np.arange(len(monthly_sales))

    #monthly_sales DF' ye 'year' ve 'month' ekleyerek sonucu 2024-7 gibi olacak bir kolon yaratıyor
    monthly_sales['year_month'] = monthly_sales['year'].astype(str) + '-' + monthly_sales['month'].astype(str)

    X = monthly_sales[['time']]  # Zaman doğrusu
    y = monthly_sales['price_per_unit']  # Fiyat doğrusu

    # x ve y ile model oluştur
    model = LinearRegression()
    model.fit(X, y)

    # future_time adında bir df yaratıyor ve içinde sadece time kolonu var. Bu kolonda monthly_saşes
    # lenght'inin üst sayısıyla yani 12 ile başlıyor ve toplam 6 row.
    future_time = pd.DataFrame({'time': np.arange(len(monthly_sales), len(monthly_sales) + 6)})

    # bu yaratılan 6 row'u predict ile doldur yani tahmin verisiyle doldur
    future_sales = model.predict(future_time)


    # iloc[-1] index location, The position of the row (e.g., 0 for the first row, -1 for the last row)
    last_year = monthly_sales['year'].iloc[-1]
    last_month = monthly_sales['month'].iloc[-1]
    last_date = datetime(year= last_year, month= last_month, day=1)


    # yukarıdaki last_date verisiyle bir takvim yaratıyor bu takvim monthly_sales'şn son tarihiyle başlıyor
    forecasted_months = [
        (last_date.replace(day=1) + pd.DateOffset(months=i)).strftime('%Y-%m') for i in range(1, 7)
    ]

    #öngörü ile olan satışı birleştir
    future_data = pd.DataFrame({'year_month': forecasted_months, 'price_per_unit': future_sales})
    combined_data = pd.concat([monthly_sales[['year_month', 'price_per_unit']], future_data])

    # Plot the forecast
    plt.figure(figsize=(12, 6))
    plt.plot(combined_data['year_month'], combined_data['price_per_unit'], marker='o', linestyle='-')
    plt.xticks(rotation=45)
    plt.title('6 Aylık Satış Tahmini', fontsize=16)
    plt.xlabel('Yıl-Ay', fontsize=12)
    plt.ylabel('Toplam Satış (Fiyat)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    return future_data

def top_selling_products(sales, products):

    product_sales = sales.groupby('product_id')['quantity'].sum().reset_index()
    product_sales = product_sales.sort_values('quantity', ascending=False).head(5)

    top_products = product_sales.merge(products, on='product_id', how= 'left')

    print("\nEn çok satan 5 ürün:")
    print(top_products)

    return top_products

def recommend_sales_increase_strategies(top_products):
    """
    Generate recommendations for increasing sales based on top-selling products.
    """
    recommendations = []
    for _, row in top_products.iterrows():
        recommendations.append(
            f"Product '{row['product_name']}' (Category: {row['category']}) is a top seller. "
            f"Consider running a marketing campaign or offering a discount to boost sales further."
        )


    return recommendations



if __name__ == "__main__":

    monthly_sales = pd.read_csv('monthly_sales_summary.csv')
    future_forecast = forecast_sales(monthly_sales)
    print("6 Aylık Tahmin:")
    print(future_forecast)
    future_forecast.to_csv('future_sales_forecast.csv', index=False)

    sales = pd.read_csv('sales_cleaned.csv')
    products = pd.read_csv('products.csv')
    top_products = top_selling_products(sales, products)
    top_products.to_csv('top_selling_products.csv', index=False)

    recommendations = recommend_sales_increase_strategies(top_products)
    print("\nSatış Artırma Önerileri:")
    for rec in recommendations:
        print(rec)
