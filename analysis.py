import pandas as pd

# Load Threat Intelligence Data
threats_df = pd.read_csv('documents/git/codeucapstone/threats.csv')
print(threats_df.head())

# Load Incident Reports Data
incidents_df = pd.read_csv('path/to/incidents.csv')
print(incidents_df.head())

