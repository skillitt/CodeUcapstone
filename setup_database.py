import sqlite3
import csv
import os

# Function to create the database and tables
def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Creating tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DIDs (
        id INTEGER PRIMARY KEY,
        did TEXT
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DIDs_Available (
        id INTEGER PRIMARY KEY,
        did TEXT
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DIDs_Used (
        id INTEGER PRIMARY KEY,
        did TEXT
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Description (
        id INTEGER PRIMARY KEY,
        description TEXT
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Reserve (
        id INTEGER PRIMARY KEY,
        reserve_info TEXT
    );
    ''')
    
    conn.commit()
    conn.close()
    print(f"Database '{db_name}' and tables created successfully.")

# Function to read the CSV and insert data into the database
def insert_data_from_csv(db_name, csv_file):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Read CSV file
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            cursor.execute('INSERT INTO DIDs (did) VALUES (?)', (row['DIDs'],))
            cursor.execute('INSERT INTO DIDs_Available (did) VALUES (?)', (row['DIDs Available'],))
            cursor.execute('INSERT INTO DIDs_Used (did) VALUES (?)', (row['DIDs Used'],))
            cursor.execute('INSERT INTO Description (description) VALUES (?)', (row['Description'],))
            cursor.execute('INSERT INTO Reserve (reserve_info) VALUES (?)', (row['Reserve'],))
    
    conn.commit()
    conn.close()
    print(f"Data from '{csv_file}' inserted into '{db_name}' successfully.")

# Main function to create the database and insert data
def main():
    db_name = 'mydatabase.db'
    csv_file = 'MOCK_DATA.csv'
    
    create_database(db_name)
    insert_data_from_csv(db_name, csv_file)
    
    print(f"Database setup and data insertion complete.")

if __name__ == '__main__':
    main()





