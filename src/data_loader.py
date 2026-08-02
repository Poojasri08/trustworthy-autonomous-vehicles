import pandas as pd

# Load the dataset
df = pd.read_csv("data/sensor_data.csv")

# Display basic information
print("Dataset loaded successfully!\n")

print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)
