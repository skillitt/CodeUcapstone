import pandas as pd

# Load the datasets
attacks_data = pd.read_csv('/Users/markdevore/documents/git/codeucapstone/attacks.csv')
#threats_data = pd.read_csv('/Users/markdevore/documents/git/codeucapstone/threats.csv')

# Inspect data
print(attacks_data.head())
#print(threats_data.head())

# Check data types and missing values
print(attacks_data.info())
#print(threats_data.info())

# Handle missing values
attacks_data = attacks_data.dropna()
#threats_data = threats_data.dropna()

# Remove duplicates
attacks_data = attacks_data.drop_duplicates()
#threats_data = threats_data.drop_duplicates()

# Convert data types if needed
# Example: Convert date columns to Type
#attacks_data['Attack Type'] = pd.to_datetime(attacks_data['Attack Type'])

# Assume you want to count the number of each attack type
attacks_by_type = attacks_data['Attack Type'].value_counts()


# Example analysis: Number of attacks over time
#attacks_by_year = attacks_data.groupby(attacks_data['Date'].dt.year).size()

# Example analysis: Distribution of threats by type
#threats_distribution = threats_data['Type'].value_counts()

import matplotlib.pyplot as plt
import seaborn as sns

# Example visualization: Distribution of attack types
plt.figure(figsize=(8, 6))
sns.barplot(x=attacks_by_type.index, y=attacks_by_type.values)
plt.title('Distribution of Attack Types')
plt.xlabel('Attack Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


