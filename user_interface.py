import tkinter as tk
''' 
Components needed for user_interface:
first screen: choose to study or to review
second screen: submit question
third screen: answer question
'''

# 2nd user screen for adding new questions to the database
larger_font = ('Calibri', 11)


def submit_question():
    question = question_entry.get("1.0", 'end-1c')
    answer = answer_entry.get("1.0", 'end-1c')
    # Add code to store to the database; print statements can be deleted
    print("Question:", question)
    print("Answer:", answer)
    # Clear entry fields after submission and move cursor back to question_entry
    question_entry.delete("1.0", tk.END)
    answer_entry.delete("1.0", tk.END)
    question_entry.focus_set()


def move_focus(event):
    if event.widget == question_entry and event.keysym == 'Tab':
        answer_entry.focus_set()
        return "break"  # Prevent default behavior
    elif event.widget == answer_entry and event.keysym == 'Tab':
        submit_button.focus_set()
        return "break"  # Prevent default behavior


def submit(event):
    if event.widget == submit_button and event.keysym == 'Return':
        submit_question()


# Create the main window
root = tk.Tk()
root.title("Create Q&As for self-study")

# Create labels, fields, and submit button
question_label = tk.Label(root, text="Question:", font=larger_font)
answer_label = tk.Label(root, text="Answer:", font=larger_font)
question_entry = tk.Text(root, height=10, width=80, font=larger_font)
answer_entry = tk.Text(root, height=10, width=80, font=larger_font)
submit_button = tk.Button(
    root, text="Submit", command=submit_question, font=larger_font)

# Bind key press events for Tab and Enter
question_entry.bind("<Tab>", move_focus)
answer_entry.bind("<Tab>", move_focus)
submit_button.bind("<Return>", submit)

# Place widgets using grid layout
question_label.grid(row=0, column=0, sticky=tk.E)
answer_label.grid(row=1, column=0, sticky=tk.E)
question_entry.grid(row=0, column=1, columnspan=2,
                    padx=5, pady=5)  # Adjusted columnspan
answer_entry.grid(row=1, column=1, columnspan=2, padx=5,
                  pady=5)    # Adjusted columnspan
submit_button.grid(row=2, column=1, columnspan=2,
                   pady=10)          # Adjusted columnspan

# Start the Tkinter event loop
root.mainloop()
