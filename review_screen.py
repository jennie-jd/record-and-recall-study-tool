import tkinter as tk
import database
import datetime

def show_next_question():
    question = database.get_question()  # Assuming you have a method to get a random question from the database
    question_label.config(text=question)
    
    # Update the last access time of the database entry
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    database.update_last_access_time(question, current_time)

root = tk.Tk()
root.title("Reviews")

root.geometry("500x400")  # Set the size of the window

question_label = tk.Label(root, text="", height=5, width=50)  # Increase the height and width of the question box
question_label.pack()

answer_entry = tk.Text(root, width=50, height=15)  # Use the Text widget for multi-line input
answer_entry.pack()

next_button = tk.Button(root, text="Next", command=show_next_question, width=10)  # Set the width of the "Next" button
next_button.pack()

exit_button = tk.Button(root, text="Exit", command=root.destroy, width=10)  # Set the width of the "Exit" button
exit_button.pack()

show_next_question()

root.mainloop()
