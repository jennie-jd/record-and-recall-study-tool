import sqlite3
import time

# Function to create database and tables
def create_database():
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS qa (
                        id INTEGER PRIMARY KEY,
                        user TEXT,
                        question TEXT,
                        answer TEXT,
                        entry_time INTEGER,
                        user_priority INTEGER
                      )''')
    conn.commit()
    conn.close()

# Function to insert data into the table
def insert_data(user, question, answer):
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    entry_time = int(time.time())  # Get current system time
    cursor.execute("INSERT INTO qa (user, question, answer, entry_time, user_priority) VALUES (?, ?, ?, ?, 0)", (user, question, answer, entry_time))
    conn.commit()
    conn.close()

# Function to retrieve data for a specific user
def retrieve_data(user):
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM qa WHERE user = ?", (user,))
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        yield row  # Yield each question-answer pair

# Function to update user priority
def update_data(user, question, answer, user_priority_update):
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE qa SET answer = ?, user_priority = user_priority + ? WHERE user = ? AND question = ?", (answer, user_priority_update, user, question))
    conn.commit()
    conn.close()

# Function to organize data based on user priority (Sample algorithm)
def organize_data():
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM qa ORDER BY user_priority DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows
