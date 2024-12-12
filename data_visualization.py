import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from data_manipulation import sales_by_category


def plot_yearly_sales(yearly_sales):

    plt.figure(figsize=(10,6))

    if len(yearly_sales) > 1:
        plt.plot(yearly_sales['year'], yearly_sales['price_per_unit'], marker='o',
                 linestyle='-', color='b', label='Yearly Sales')
    else:
        plt.bar(yearly_sales['year'], yearly_sales['price_per_unit'], color='blue', alpha=0.7, label='Yearly Sales',
                width=0.5)
        plt.text(yearly_sales['year'].iloc[0], yearly_sales['price_per_unit'].iloc[0],
                 f"{yearly_sales['price_per_unit'].iloc[0]:.2f}", ha='center', va='bottom', fontsize=12)




    plt.title('Yıllık Satış Trendleri', fontsize=16)
    plt.xlabel('Yıl', fontsize=12)
    plt.ylabel('Toplam Satış (Fiyat)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()

    plt.savefig('yearly_sales_chart.png')  # Save the chart
    print("Chart saved as 'yearly_sales_chart.png'")

    plt.show(block=False)  # Display without blocking
    plt.pause(3)  # Keep it visible for 3 seconds
    plt.close()



def plot_monthly_sales(monthly_sales):
    # Combine year and month for a readable x-axis label
    monthly_sales['year_month'] = monthly_sales['year'].astype(str) + '-' + monthly_sales['month'].astype(str)

    # Plot bar chart using Seaborn for better aesthetics
    plt.figure(figsize=(12, 6))
    sns.barplot(
        x='year_month', y='price_per_unit', data=monthly_sales, palette='Blues_d', hue='year_month', dodge=False
    )
    plt.title('Aylık Satış Trendi', fontsize=16)
    plt.xlabel('Yıl-Ay', fontsize=12)
    plt.ylabel('Toplam Satış (Fiyat)', fontsize=12)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def plot_category_sales(product_sales_summary):
    plt.figure(figsize=(8,8))
    plt.pie(
        sales_by_category['total_revenue'],
        labels=sales_by_category['category'],
        autopct='%1.1f%%',
        startangle=140,
        colors=plt.cm.Paired.colors
    )
    plt.title('Ürün Kategorilerime Göre Satış Dağılımı', fontsize=16)
    plt.show()

if __name__ == "__main__":
    sales_by_category = pd.read_csv('product_sales_summary.csv')
    plot_category_sales(sales_by_category)

    monthly_sales = pd.read_csv('monthly_sales_summary.csv')
    plot_monthly_sales(monthly_sales)

    yearly_sales = pd.read_csv('yearly_sales_summary.csv')
    plot_yearly_sales(yearly_sales)

