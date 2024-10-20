# utils/database_helper.py

import sqlite3
from config.config import DB_PATH

def connect_db():
    conn = sqlite3.connect(DB_PATH)
    return conn

def store_daily_summary(summary):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_summary (
            date TEXT PRIMARY KEY,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_condition TEXT
        )
    ''')
    cursor.execute('''
        INSERT OR REPLACE INTO daily_summary 
        VALUES (?, ?, ?, ?, ?)
    ''', (summary['date'], summary['avg_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_condition']))
    conn.commit()
    conn.close()
