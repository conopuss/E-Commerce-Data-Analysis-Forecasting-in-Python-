import pandas as pd

def clean_data():
    sales = pd.read_csv('sales.csv')
    products = pd.read_csv('products.csv')
    customers = pd.read_csv('customers.csv')
    feedback = pd.read_csv('feedback.csv')

    #print("Satış verileri:")
    #print(sales.head())
    #print("\nÜrün verileri:")
    #print(products.head())
    #print("\nMüşteri verileri:")
    #print(customers.head())
    #print("\nGeri bildirim verileri:")
    #print(feedback.head())

    sales = sales.merge(products[['product_id','price']], on='product_id', how='left')

    sales['price_per_unit'] = sales['price_per_unit'].fillna(sales['price'])
    sales.drop(columns=['price'], inplace=True)

    print("\nEksik değerler girildikten sonra fiyatlar:")
    print(sales.isnull().sum())

    sales['sales_date'] = sales['sales_date'].str.replace('/','-',regex=False)
    sales['sales_date'] = pd.to_datetime(sales['sales_date'], errors='coerce')

    invalid_dates = sales[sales['sales_date'].isnull()]
    if not invalid_dates.empty:
        print("\nGeçersiz tarihleri içeren satırlar kaldırıldı")
        print(invalid_dates)
    sales = sales[sales['sales_date'].notnull()]

    sales.to_csv('sales_cleaned.csv', index=False)
    print("\nDüzeltilmiş veri 'sales_cleaned.csv' dosyasında saklandı.")

    feedback = feedback.dropna(subset=['rating'])
    feedback['feedback_text'] = feedback['feedback_text'].fillna('').str.strip()
    feedback = feedback[feedback['feedback_text'] != '']

    print("\nEksik veya boş alanları olan geri bildirim verileri kaldırıldı.")

    feedback.to_csv('feedback_cleaned.csv',index=False)
    print("Temizlenmiş geri bildirim verisi 'feedback_celaned.csv' olarak kayededildi.")

    return sales, feedback, products

if __name__ == '__main__':
    sales_cleaned, feedback_cleaned, products_cleaned = clean_data()
    print("\nSatış verilerinden örnekler:")
    print(sales_cleaned.head())
    print("\nGeri bildirim verilerinden örnekler:")
    print(feedback_cleaned.head())
    print("\nÜrün verilerinden örnekler:")
    print(products_cleaned.head())
