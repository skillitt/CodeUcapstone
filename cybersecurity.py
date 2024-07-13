import pandas as pd

# Load the datasets
attacks_data = pd.read_csv('/Users/myusername/documents/git/codeucapstone/attacks.csv')
threats_data = pd.read_csv('/Users/myusername/documents/git/codeucapstone/threats.csv')

# Inspect data
print(attacks_data.head())
print(threats_data.head())

# Check data types and missing values
print(attacks_data.info())
print(threats_data.info())

# Handle missing values
attacks_data = attacks_data.dropna()
threats_data = threats_data.dropna()

# Remove duplicates
attacks_data = attacks_data.drop_duplicates()
threats_data = threats_data.drop_duplicates()

# Convert data types if needed
# Example: Convert date columns to datetime
attacks_data['Date'] = pd.to_datetime(attacks_data['Date'])

# Example analysis: Number of attacks over time
attacks_by_year = attacks_data.groupby(attacks_data['Date'].dt.year).size()

# Example analysis: Distribution of threats by type
threats_distribution = threats_data['Type'].value_counts()

import matplotlib.pyplot as plt
import seaborn as sns

# Example visualization: Attacks over time
plt.figure(figsize=(10, 6))
sns.lineplot(x=attacks_by_year.index, y=attacks_by_year.values)
plt.title('Number of Cybersecurity Attacks Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.grid(True)
plt.show()

# Example visualization: Threats distribution
plt.figure(figsize=(8, 6))
threats_distribution.plot(kind='bar')
plt.title('Distribution of Threats by Type')
plt.xlabel('Threat Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
