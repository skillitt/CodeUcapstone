import pandas as pd
import configparser
import os

# Define the config file path
config_file = 'config.ini'
config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), config_file)

# Check if the config file exists
if not os.path.isfile(config_file_path):
    raise FileNotFoundError(f"Config file not found at {config_file_path}")

# Print the path to the config file for debugging
print(f"Reading config file from: {config_file_path}")

# Load configuration
config = configparser.ConfigParser()
config.read(config_file_path)

# Print sections and options for debugging
print("Config sections:", config.sections())
if 'paths' in config:
    print("Paths options:", config['paths'].items())

if 'paths' not in config:
    raise KeyError("The 'paths' section is missing in the config.ini file")

# Get paths from configuration
attacks_path = config['paths']['attacks_csv']
threats_path = config['paths']['threats_csv']
output_path = config['paths']['output_csv']

# Ensure paths are relative to the script location
base_path = os.path.dirname(os.path.abspath(__file__))
attacks_path = os.path.join(base_path, attacks_path)
threats_path = os.path.join(base_path, threats_path)
output_path = os.path.join(base_path, output_path)

# Load the datasets
attacks_df = pd.read_csv(attacks_path)
threats_df = pd.read_csv(threats_path)

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
merged_df.to_csv(output_path, index=False)

print(f"Datasets merged and saved to {output_path}")
