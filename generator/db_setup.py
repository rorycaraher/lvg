import sqlite3

def initialize_db():
    conn = sqlite3.connect('generator/data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS level_values (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value1 REAL,
            value2 REAL,
            value3 REAL,
            value4 REAL,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
