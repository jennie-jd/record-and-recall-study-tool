import tkinter as tk
import database
import study_screen
import review_screen

''' 
To do: add password function in addition to username
'''

# 1st screen to register users and choose to study or review
display_font = ('Calibri', 11)

# Database of users and passwords
users = {
    "user1": "password1",
    "user2": "password2",
    # Add more users as needed
}

# Counter for login attempts
login_attempts = 0

def authenticate(username, password):
    global login_attempts
    if username in users and users[username] == password:
        return True
    else:
        login_attempts += 1
        return False

def login(username_entry, password_entry, login_label):
    global login_attempts
    username = username_entry.get()
    password = password_entry.get()
    if authenticate(username, password):
        login_label.config(text="Login successful!", fg="green")
        study_or_review_window(username)
    else:
        if login_attempts < 5:
            login_label.config(text="Incorrect username or password. Please try again.")
        else:
            login_label.config(text="Too many login attempts. Program will now exit.", fg="red")
            root.after(2000, root.quit)

def study_or_review_window(username):
    root.destroy()  # Close the login window
    root = tk.Tk()
    root.title("Study or Review")
    root.geometry("300x150")

    label = tk.Label(root, text="Welcome, " + username + "! Choose an option:", font=display_font)
    label.pack(pady=10)

    study_button = tk.Button(root, text="Study", font=display_font, command=lambda: study_or_review("study"))
    study_button.pack(pady=5)

    review_button = tk.Button(root, text="Review", font=display_font, command=lambda: study_or_review("review"))
    review_button.pack(pady=5)

    root.mainloop()

def main():
    global root
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x200")

    username_label = tk.Label(root, text="Username:", font=display_font)
    username_label.pack(pady=5)

    username_entry = tk.Entry(root, font=display_font)
    username_entry.pack(pady=5)

    password_label = tk.Label(root, text="Password:", font=display_font)
    password_label.pack(pady=5)

    password_entry = tk.Entry(root, show="*", font=display_font)
    password_entry.pack(pady=5)

    login_button = tk.Button(root, text="Login", font=display_font,
                             command=lambda: login(username_entry, password_entry, login_label))
    login_button.pack(pady=5)

    login_label = tk.Label(root, text="", font=display_font)
    login_label.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
