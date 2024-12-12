import pandas as pd
import requests

def fetch_exchange_rate():
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        exchange_rate = data['rates']['TRY']
        print(f"USD/TRY kuru: {exchange_rate}")
        return exchange_rate
    else:
        raise Exception("Kur edinimi başarılamadı")
def convert_to_usd(sales_file, output_file):

    sales = pd.read_csv(sales_file)
    exchange_rate = fetch_exchange_rate()

    sales['price_per_unit_usd'] = sales['price_per_unit'] * (1/ exchange_rate)
    sales.to_csv(output_file, index = False)
    print(f"Satış verilerinin USD döviz karşılıkları {output_file} dosyasına kaydedildi")

if __name__ == '__main__':
    convert_to_usd('sales_cleaned.csv', 'sales_in_usd.csv')


