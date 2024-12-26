import sqlite3
import pandas as pd

def create_connection():
    conn = sqlite3.connect('database.db')
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recruiters (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            company TEXT NOT NULL,
            is_cmr BOOLEAN NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def update_database(df):
    conn = create_connection()
    cursor = conn.cursor()
    create_tables()
    
    # Remove duplicates and rows with NULL values
    df.drop_duplicates(subset=['Name', 'Email'], inplace=True)
    df.dropna(inplace=True)
    
    for _, row in df.iterrows():
        cursor.execute('''
            INSERT OR REPLACE INTO recruiters (name, email, company, is_cmr)
            VALUES (?, ?, ?, ?)
        ''', (row['Name'], row['Email'], row['Company'], row['IsCMR']))
    
    conn.commit()
    conn.close()

def get_recruiters():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM recruiters')
    recruiters = cursor.fetchall()
    conn.close()
    return recruiters

def clear_all_recruiters():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM recruiters')
    conn.commit()
    conn.close()