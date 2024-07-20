import pandas as pd

# Load datasets
cybersecurity_attacks_df = pd.read_csv('/home/devore_m/GitHub/cybersecurity/cybersecurity_attacks.csv')
malicious_phish_df = pd.read_csv('/home/devore_m/GitHub/cybersecurity/malicious_phish.csv')  


# Check the columns of both dataframes
print(cybersecurity_attacks_df.columns)
print(malicious_phish_df.columns)

# Ensure both dataframes have the 'date' column before merging
if 'Year' in cybersecurity_attacks_df.columns and 'year' in malicious_phish_df.columns:
    # Merge datasets on the 'date' column
    merged_df = pd.merge(cybersecurity_attacks_df, malicious_phish_df, on='date')

    # Save merged dataset
    merged_df.to_csv('/home/devore_m/GitHub/cybersecurity/merged_data.csv', index=False)
else:
    print("One of the dataframes does not have the 'year' column")

