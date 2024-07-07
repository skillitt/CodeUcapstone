import pandas as pd

# File paths
attacks_file = "attacks.csv"
threats_file = "threats.csv"

# Load datasets
attacks_data = pd.read_csv(attacks_file)
threats_data = pd.read_csv(threats_file)

# Example: Print first few rows of each dataset
print("Attacks Data:")
print(attacks_data.head())

print("\nThreats Data:")
print(threats_data.head())




