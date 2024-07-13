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
cyberthreat_by_type = cyberthreat_data['Cyber Threat'].value_counts()

import matplotlib.pyplot as plt
import seaborn as sns

# Example visualization: Distribution of attack types
plt.figure(figsize=(8, 6))
sns.barplot(x=cyberthreat_by_type.index, y=cyberthreat_by_type.values)
plt.title('Distribution of Cyber Threat')
plt.xlabel('Cyber Threat')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()