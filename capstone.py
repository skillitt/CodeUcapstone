import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
cleaned_file_path = '/Users/markdevore/Documents/git/CodeUcapstone/cleaned_cybersecurity_attacks.csv'
df = pd.read_csv(cleaned_file_path)

# Display the first few rows of the dataset to inspect
print("Initial dataset:")
print(df.head())

# Ensure the 'Timestamp' column is correctly parsed as datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Visualization 1: Bar Plot (number of attacks per year)
plt.figure(figsize=(10, 6))
# Extract year from the 'Timestamp' column
df['Year'] = df['Timestamp'].dt.year
attacks_per_year = df['Year'].value_counts().sort_index()
sns.barplot(x=attacks_per_year.index, y=attacks_per_year.values, palette='viridis')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.title('Number of Cybersecurity Attacks per Year')
plt.xticks(rotation=45)
plt.show()

# Visualization 2: Heatmap (correlation matrix of numerical features)
plt.figure(figsize=(10, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Features')
plt.show()

# Visualization 3: Line Plot (trend of attacks over time)
plt.figure(figsize=(10, 6))
# Set 'Timestamp' as the index
df.set_index('Timestamp', inplace=True)
# Resample the data by month and count the number of attacks per month
attacks_per_month = df.resample('M').size()
sns.lineplot(x=attacks_per_month.index, y=attacks_per_month.values, marker='o')
plt.xlabel('Date')
plt.ylabel('Number of Attacks')
plt.title('Trend of Cybersecurity Attacks Over Time')
plt.xticks(rotation=45)
plt.show()
