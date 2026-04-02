import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv("data.csv", encoding='ISO-8859-1')

# 1. First 5 rows
print("First 5 rows:\n", df.head())

# 2. Dataset info
print("\nDataset Info:\n")
df.info()

# 3. Missing values
print("\nMissing Values:\n", df.isnull().sum())

# 4. Summary statistics
print("\nSummary Statistics:\n", df.describe())

df = pd.read_csv("data.csv", encoding='ISO-8859-1')

# 1. Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# 2. Remove missing CustomerID
df = df.dropna(subset=['CustomerID'])

# 3. Remove negative Quantity
df = df[df['Quantity'] > 0]

# 4. Remove negative UnitPrice
df = df[df['UnitPrice'] > 0]

# 5. Check cleaned data
print("After Cleaning:\n")
print(df.info())
print("\nRemaining Data:\n", df.shape)

df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
print("Total Revenue:", df['TotalPrice'].sum())
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products:\n", top_products)
top_countries = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Countries:\n", top_countries)
df['Month'] = df['InvoiceDate'].dt.to_period('M')

monthly_sales = df.groupby('Month')['TotalPrice'].sum()

print("\nMonthly Sales:\n", monthly_sales)
print(df.head())


top_products.plot(kind='bar')
plt.title("Top 5 Products")
plt.show()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.show()