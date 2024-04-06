import tkinter as tk

''' 
first screen: choose to study or to review
second screen: submit question
third sreen: answer question
'''

def submit_question():
    question = question_entry.get("1.0",'end-1c')
    answer = answer_entry.get("1.0",'end-1c')
    # Here you can add code to store the question and answer in the database
    print("Question:", question)
    print("Answer:", answer)
    # Clear the entry fields after submission
    question_entry.delete(0, tk.END)
    answer_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Record questions and answers as you study")

# Create labels
question_label = tk.Label(root, text="Question:")
answer_label = tk.Label(root, text="Answer:")

# Create entry fields with adjusted height and width
question_entry = tk.Text(root, height = 20, width = 40)
answer_entry = tk.Text(root, height = 20, width = 40)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_question)

# Place widgets using grid layout
question_label.grid(row=0, column=0, sticky=tk.E)
answer_label.grid(row=1, column=0, sticky=tk.E)
question_entry.grid(row=0, column=1, padx=5, pady=5)
answer_entry.grid(row=1, column=1, padx=5, pady=5)
submit_button.grid(row=2, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
