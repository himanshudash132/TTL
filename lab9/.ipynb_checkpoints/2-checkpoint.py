#Q3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Automobile.csv')

# 1. Handle the missing values for Price column
# Assuming missing values are represented as NaN
df['price'].fillna(df['price'].mean(), inplace=True)

# 2. Get the values from Price column into a numpy.ndarray
price_array = df['price'].values

# 3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
min_price = np.min(price_array)
max_price = np.max(price_array)
avg_price = np.mean(price_array)
std_dev_price = np.std(price_array)

# Print the statistics
print(f"Minimum Price: {min_price}")
print(f"Maximum Price: {max_price}")
print(f"Average Price: {avg_price}")
print(f"Standard Deviation of Price: {std_dev_price}")

# 4. Make a pie chart for all car makers
car_makers = df['make'].value_counts()
plt.figure(figsize=(10, 8))
plt.pie(car_makers, labels=car_makers.index, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart of Car Makers')
plt.legend(title = 'car maker')
plt.show()