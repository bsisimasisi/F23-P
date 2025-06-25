import pandas as pd
import numpy as np
#1
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

df.columns = [col.lower().replace(" ", "_") for col in df.columns]

print("First 3 rows:")
print(df.head(3))

mean_age = df['age'].mean()
print("\nMean age:", mean_age)

print("\nName and City columns:")
print(df[['first_name', 'city']])

df['salary'] = np.random.randint(50000, 100000, size=len(df))
print("\nDataFrame with Salary:")
print(df)

print("\nSummary Statistics:")
print(df.describe(include='all'))


#2
sales_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(sales_data)

print("\nMaximum Sales and Expenses:")
print(sales_and_expenses[['Sales', 'Expenses']].max())

print("\nMinimum Sales and Expenses:")
print(sales_and_expenses[['Sales', 'Expenses']].min())

print("\nAverage Sales and Expenses:")
print(sales_and_expenses[['Sales', 'Expenses']].mean())




#3
expenses_data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expenses = pd.DataFrame(expenses_data)

expenses = expenses.set_index('Category')

print("\nMaximum expense for each category:")
print(expenses.max(axis=1))

print("\nMinimum expense for each category:")
print(expenses.min(axis=1))

print("\nAverage expense for each category:")
print(expenses.mean(axis=1))

