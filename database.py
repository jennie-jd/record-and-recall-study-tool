import sqlite3

# Function to create database and tables
def create_database():
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS qa (
                        id INTEGER PRIMARY KEY,
                        user TEXT,
                        question TEXT,
                        answer TEXT
                      )''')
    conn.commit()
    conn.close()

# Function to insert data into the table
def insert_data(user, question, answer):
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO qa (user, question, answer) VALUES (?, ?, ?)", (user, question, answer))
    conn.commit()
    conn.close()

# Function to retrieve data from the table
def retrieve_data():
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM qa")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to update data in the table
def update_data(user, new_answer):
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE qa SET answer = ? WHERE user = ?", (new_answer, user))
    conn.commit()
    conn.close()

# Function to delete data from the table
def delete_data(user):
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM qa WHERE user = ?", (user,))
    conn.commit()
    conn.close()

# Main code
if __name__ == "__main__":
    # Create the database and tables
    create_database()
    
    # Insert data into the table
    insert_data("Mary", "Are you okay?", "Yes, great")
    
    # Retrieve data from the table
    entries = retrieve_data()
    
    # Print the retrieved entries
    print("Retrieved Entry:")
    for entry in entries:
        print("User:", entry[1])
        print("Question:", entry[2])
        print("Answer:", entry[3])
    
    # Update data in the table
    update_data("Mary", "Yes, I'm doing fine")
    
    # Retrieve and print updated data
    updated_entries = retrieve_data()
    print("\nUpdated Entry:")
    for entry in updated_entries:
        print("User:", entry[1])
        print("Question:", entry[2])
        print("Answer:", entry[3])
    
    # Delete data from the table
    delete_data("Mary")
    
    # Verify deletion by retrieving data again
    deleted_entries = retrieve_data()
    if not deleted_entries:
        print("\nData deleted successfully!")
    else:
        print("\nDeletion failed.")



# import sqlite3

# # Connect to SQLite database
# conn = sqlite3.connect('questions.db')
# c = conn.cursor()

# # Create a table to store questions
# def store_new_entry(question, answer):
#     c.execute('''INSERT INTO questions (question, answer) VALUES (?, ?)''', (question, answer))
#     conn.commit()

# def delete_entry(id):
#     c.execute('''DELETE FROM questions WHERE id = ?''', (id,))
#     conn.commit()

# def update_entry(id, status):
#     pass

# c.execute('''CREATE TABLE IF NOT EXISTS questions
#              (id INTEGER PRIMARY KEY AUTOINCREMENT, 
#              question TEXT, 
#              answer TEXT, 
#              last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

# # Close the connection
# conn.close()
