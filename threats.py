from matplotlib import pyplot as plt
import pandas as pd

# Load the datasets

threats_data = pd.read_csv('/Users/markdevore/documents/git/codeucapstone/threats.csv')

# Inspect data

print(threats_data.head())

# Check data types and missing values

print(threats_data.info())

# Handle missing values

threats_data = threats_data.dropna()

# Remove duplicates

threats_data = threats_data.drop_duplicates()

# Assume you want to count the number of each attack type
threats_by_type = threats_data['Severity'].value_counts()

#import matplotlib.pyplot as plt
import seaborn as sns

# Example visualization: Distribution of attack types
plt.figure(figsize=(8, 6))
sns.barplot(x=threats_by_type.index, y=threats_by_type.values)
plt.title('Distribution of Severity')
plt.xlabel('Severity')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()