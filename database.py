import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('questions.db')
c = conn.cursor()

# Create a table to store questions
c.execute('''CREATE TABLE IF NOT EXISTS questions
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             question TEXT, 
             answer TEXT, 
             last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

# Commit changes and close connection
conn.commit()
conn.close()
