import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('questions.db')
c = conn.cursor()

# Create a table to store questions
def store_new_entry(question, answer):
    c.execute('''INSERT INTO questions (question, answer) VALUES (?, ?)''', (question, answer))
    conn.commit()

def delete_entry(id):
    c.execute('''DELETE FROM questions WHERE id = ?''', (id,))
    conn.commit()

def update_entry(id, status):
    pass

c.execute('''CREATE TABLE IF NOT EXISTS questions
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             question TEXT, 
             answer TEXT, 
             last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

# Close the connection
conn.close()
