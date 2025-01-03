import sqlite3

def create_db():
    conn = sqlite3.connect('officials.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS officials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            state TEXT NOT NULL,
            district TEXT NOT NULL,
            block TEXT NOT NULL,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            contact TEXT,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()