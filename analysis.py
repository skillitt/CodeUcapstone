import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(threats_path, incidents_path):
    threats_df = pd.read_csv(threats_path)
    incidents_df = pd.read_csv(incidents_path)
    return threats_df, incidents_df

def clean_data(df):
    df.dropna(inplace=True)
    return df

def analyze_data(threats_df, incidents_df):
    threat_counts = threats_df['threat_type'].value_counts()
    incident_counts = incidents_df['incident_type'].value_counts()
    return threat_counts, incident_counts

def visualize_data(threat_counts, incident_counts):
    plt.figure(figsize=(10, 5))
    sns.barplot(x=threat_counts.index, y=threat_counts.values)
    plt.title('Threat Counts by Type')
    plt.xlabel('Threat Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(10, 5))
    sns.barplot(x=incident_counts.index, y=incident_counts.values)
    plt.title('Incident Counts by Type')
    plt.xlabel('Incident Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

def main():
    threats_path = 'C:/Users/markdevore/Documents/git/CodeUcapstone/data/threats.csv'
    incidents_path = 'C:/Users/markdevore/Documents/git/CodeUcapstone/dataincidents.csv'
    
    threats_df, incidents_df = load_data(threats_path, incidents_path)
    threats_df = clean_data(threats_df)
    incidents_df = clean_data(incidents_df)
    
    threat_counts, incident_counts = analyze_data(threats_df, incidents_df)
    visualize_data(threat_counts, incident_counts)
    
    with open('findings.txt', 'w') as f:
        f.write("Threat Counts by Type:\n")
        f.write(threat_counts.to_string())
        f.write("\n\nIncident Counts by Type:\n")
        f.write(incident_counts.to_string())

if __name__ == '__main__':
    main()



