import pandas as pd

# Load the datasets
attacks_df = pd.read_csv('/Users/markdevore/Documents/git/CodeUcapstone/cybersecurity_attacks.csv')
threats_df = pd.read_csv('/Users/markdevore/Documents/git/codeucapstone/cyberthreat.csv')

# Print column names
print("Columns in attacks_df:", attacks_df.columns)
print("Columns in threats_df:", threats_df.columns)

# Perform cleaning datasets
attacks_df.dropna(inplace=True)
threats_df.dropna(inplace=True)

# Add a unique identifier column for merging
attacks_df['merge_id'] = range(len(attacks_df))
threats_df['merge_id'] = range(len(threats_df))

# Merge the datasets on the new 'merge_id' column
merged_df = pd.merge(attacks_df, threats_df, on='merge_id', how='inner')

# Drop the 'merge_id' column after merging
merged_df.drop(columns=['merge_id'], inplace=True)

# Save the cleaned and merged dataset to a new CSV file
merged_df.to_csv('/Users/markdevore/Documents/git/codeucapstone/merged_datasets.csv', index=False)

print("Datasets merged and saved to cleaned_cybersecurity_attacks.csv")

