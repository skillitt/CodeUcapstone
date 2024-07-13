import pandas as pd

# Load the datasets

cyberthreat_data = pd.read_csv('/Users/markdevore/documents/git/codeucapstone/cyberthreat.csv')

# Inspect data

print(cyberthreat_data.head())

# Check data types and missing values

print(cyberthreat_data.info())

# Handle missing values

cyberthreat_data = cyberthreat_data.dropna()

# Remove duplicates

cyberthreat_data = cyberthreat_data.drop_duplicates()

# Assume you want to count the number of each attack type
#attacks_by_type = attacks_data['Attack Type'].value_counts()

# Example analysis: Distribution of threats by type
#threats_distribution = threats_data['Type'].value_counts()

import matplotlib.pyplot as plt
import seaborn as sns

# Example visualization: Distribution of attack types
#plt.figure(figsize=(8, 6))
#sns.barplot(x=attacks_by_type.index, y=attacks_by_type.values)
#plt.title('Distribution of Attack Types')
#plt.xlabel('Attack Type')
#plt.ylabel('Count')
#plt.xticks(rotation=45)
#plt.show()