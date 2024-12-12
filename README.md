Turkish:
# AI Uygulama Projesi 2

Bu proje, Python ve veri işleme becerilerini geliştirmek için tasarlanmış kapsamlı bir veri analizi ve görselleştirme işlem hattıdır. Proje, veri temizleme, analiz, tahmin ve otomasyon gibi çeşitli adımları içerir.

## Özellikler
- **Veri Temizleme:** Eksik değerlerin, yanlış formatların ve geçersiz kayıtların işlenmesi.
- **Veri Analizi:** Yıllık, aylık ve günlük satış özetleri oluşturma ve müşteri harcama trendlerini belirleme.
- **Tahmin:** Lineer regresyon modeli kullanarak önümüzdeki 6 ayın satışlarını tahmin etme.
- **Görselleştirme:** Yıllık trendler, aylık satışlar ve kategori bazlı satış dağılımı için grafikler oluşturma.
- **Otomasyon:** Tüm `.csv` dosyalarını okuyup işleyen ve kapsamlı raporlar oluşturan bir script.

## Teslimatlar
- **sales_summary.xlsx:** Birden fazla sayfa içeren konsolide satış raporları.
- **future_predictions.csv:** Önümüzdeki 6 aya ait tahmini satışlar.
- **top_products.csv:** En çok satan ilk 5 ürünün listesi.
- **case_automation.py:** Veri işleme hattını otomatikleştiren script.

## Araçlar ve Teknolojiler
- Python (pandas, matplotlib, seaborn, scikit-learn)
- Excel Otomasyonu
- Sürüm kontrolü için Git
-------------------------------------------------------------

English
# AI Practice Project 2

This project is a comprehensive data analysis and visualization pipeline designed to enhance skills in Python and data manipulation. The project consists of several steps, including data cleaning, analysis, forecasting, and automation.

## Features
- **Data Cleaning:** Handle missing values, incorrect formats, and invalid entries.
- **Data Analysis:** Generate yearly, monthly, and daily sales summaries and identify customer spending trends.
- **Forecasting:** Predict the next 6 months of sales using a linear regression model.
- **Visualization:** Create charts for yearly trends, monthly sales, and category-wise sales distribution.
- **Automation:** A script that reads all `.csv` files, processes them, and generates comprehensive reports in an Excel file.

## Deliverables
- **sales_summary.xlsx:** Consolidated sales reports with multiple sheets.
- **future_predictions.csv:** Forecasted sales for the next 6 months.
- **top_products.csv:** List of top 5 best-selling products.
- **case_automation.py:** Script to automate the data processing pipeline.

## Tools & Technologies
- Python (pandas, matplotlib, seaborn, scikit-learn)
- Excel Automation
- Git for version control

-------------------------------------------------------
 Turkish
 
 Veri Analizi ve Tahmin
Senaryo
Bir e-ticaret şirketi, müşteri harcamalarını analiz etmek, ürün satışlarını artırmak için önerilerde bulunmak ve gelecekteki satışları tahmin etmek istiyor. Şirket sana aşağıdaki veri setlerini sağlamıştır:
1.	customers.csv: Müşteri bilgileri.
2.	products.csv: Ürün bilgileri.
3.	sales.csv: Satış bilgileri.
4.	feedback.csv: Müşteri geri bildirimleri.
Görevler
1.	Veri Temizleme ve Hazırlık
o	sales.csv dosyasındaki eksik fiyat verilerini products.csv dosyasından tamamla.
o	Tarih formatı hatalı olan kayıtları düzelt.
o	Müşteri geri bildirimlerinden (feedback.csv) eksik alanları temizle.
2.	Veri Manipülasyonu
o	Satış verisini yıllık, aylık ve günlük bazda gruplandırarak özetle.
o	Müşteri harcamalarını analiz ederek toplam harcama sütunu ekle (total_spent).
o	Ürün kategorisine göre satış dağılımını çıkar.
3.	Veri Görselleştirme
o	Aşağıdaki grafikleri oluştur:
	Yıllık satış trendlerini gösteren bir çizgi grafiği.
	Aylık satışları gösteren bir bar grafiği.
	Ürün kategorilerine göre satışları gösteren bir pasta grafiği.
4.	Tahmin ve Öneriler
o	Geçmiş satış verilerine dayanarak önümüzdeki 6 ay için satış tahmini yap.
o	En çok satan 5 ürünü tespit et ve satışları artırmak için önerilerde bulun.
5.	Döviz İşlemleri
o	USD/TRY kurunu bir API’den çekerek toplam satış verisini USD’ye çevir.
6.	Otomasyon Görevi
o	Bir script yaz ve bu script şu işlemleri otomatikleştirsin:
	Klasördeki tüm *.csv dosyalarını oku.
	Verileri temizle, analiz et ve rapor oluştur.
	Oluşturulan raporları bir Excel dosyasına birden fazla sheet ile kaydet.
________________________________________
Teslimat
1.	Aşağıdaki dosyaları teslim et:
o	case_analiz.py: Verileri temizlemek, analiz etmek ve görselleştirmek için kod.
o	case_otomasyon.py: Tüm süreci otomatikleştiren script.
2.	Çıktılar:
o	sales_summary.xlsx: Tüm analizlerin ve grafikleri içeren bir Excel dosyası.
o	future_predictions.csv: Satış tahminleri.
o	top_products.csv: En çok satan ürünlerin listesi.

----------------------------

English:
Data Analysis and Forecasting

Scenario
An e-commerce company wants to analyze customer spending, provide recommendations to boost product sales, and predict future sales. The company has provided you with the following datasets:

customers.csv: Customer information.
products.csv: Product information.
sales.csv: Sales information.
feedback.csv: Customer feedback.
Tasks

Data Cleaning and Preparation

Complete missing price data in sales.csv using products.csv.
Fix records with incorrect date formats.
Clean missing fields from customer feedback in feedback.csv.
Data Manipulation

Summarize sales data by grouping it yearly, monthly, and daily.
Analyze customer spending and add a total_spent column.
Generate sales distribution by product category.
Data Visualization

Create the following charts:
A line chart showing yearly sales trends.
A bar chart showing monthly sales.
A pie chart showing sales distribution by product categories.
Forecasting and Recommendations

Predict sales for the next six months based on historical data.
Identify the top 5 best-selling products and provide recommendations to increase their sales.
Currency Conversion

Fetch the USD/TRY exchange rate from an API and convert total sales data into USD.
Automation Task

Write a script to automate the following processes:
Read all *.csv files in the directory.
Clean, analyze, and generate reports from the data.
Save the generated reports in an Excel file with multiple sheets.
Deliverables

Submit the following files:
case_analiz.py: Code for cleaning, analyzing, and visualizing the data.
case_otomasyon.py: Script automating the entire process.
Outputs:
sales_summary.xlsx: Excel file containing all analyses and charts.
future_predictions.csv: Future sales forecasts.
top_products.csv: List of top-selling products.

