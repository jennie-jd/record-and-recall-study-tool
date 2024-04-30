import tkinter as tk
import database
import welcome_screen
import study_screen

# In development

# 3rd user screen for reviewing past questions
class ReviewScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.database = database.Database()  # Assuming you have a Database class in database module
        self.create_widgets()

    def create_widgets(self):
        # Create and place widgets here
        self.label = tk.Label(self, text="Review Screen")
        self.label.pack()

        # Example: Displaying past questions from the database
        past_questions = self.database.get_past_questions()  # Assuming a method get_past_questions() to retrieve past questions
        for question in past_questions:
            question_label = tk.Label(self, text=question)
            question_label.pack()

        # Example: Adding a button to go back to the welcome screen
        self.back_button = tk.Button(self, text="Back to Welcome Screen", command=self.go_to_welcome_screen)
        self.back_button.pack()

    def go_to_welcome_screen(self):
        self.master.switch_frame(welcome_screen.WelcomeScreen)  # Assuming you have a method switch_frame in your WelcomeScreen class

if __name__ == "__main__":
    app = tk.Tk()
    app.title("Review Screen")
    app.geometry("400x300")
    review_screen = ReviewScreen(app)
    review_screen.pack(fill="both", expand=True)
    app.mainloop()
