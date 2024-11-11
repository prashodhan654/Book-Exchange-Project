import tkinter as tk
from tkinter import messagebox
import uuid

# In-memory data storage (simplified version)
users = {}  # Stores username and password
books = []  # List of books with title, genre, status
notifications = {}  # Stores notifications for each user

# Register a new user
def register_user(username, password):
    if username in users:
        messagebox.showerror("Error", "Username already exists")
    else:
        users[username] = password
        notifications[username] = []  # Initialize empty notifications for new user
        messagebox.showinfo("Success", "User registered successfully")
        open_login_screen()  # Go back to the login screen after registration

# Log in a user
def login_user(username, password):
    if username in users and users[username] == password:
        messagebox.showinfo("Success", "Login successful")
        open_main_application(username)  # Open the main screen after login
    else:
        messagebox.showerror("Error", "Invalid credentials")

# Add a book to the listing
def add_book(title, genre):
    book_id = str(uuid.uuid4())  # Unique book ID
    books.append({"id": book_id, "title": title, "genre": genre, "status": "available"})
    messagebox.showinfo("Success", f"Book '{title}' added successfully")

# Search books by title or genre
def search_books(query):
    return [book for book in books if query.lower() in book["title"].lower() or query.lower() in book["genre"].lower()]

# Display the list of available books
def open_book_listing():
    for widget in root.winfo_children():
        widget.destroy()  # Clear the current window

    tk.Label(root, text="Available Books").pack(pady=10)
    book_listbox = tk.Listbox(root, width=50, height=10)
    book_listbox.pack()

    # Add books to the listbox
    for book in books:
        book_listbox.insert(tk.END, f"{book['title']} - {book['genre']} ({book['status']})")

    tk.Button(root, text="Back", command=lambda: open_main_application(current_user)).pack(pady=10)

# Display search results
def open_search_results():
    query = search_entry.get()
    result = search_books(query)

    # Clear the window and display results
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Search Results").pack(pady=10)
    if result:
        for book in result:
            tk.Label(root, text=f"{book['title']} - {book['genre']} ({book['status']})").pack()
    else:
        tk.Label(root, text="No books found").pack()

    tk.Button(root, text="Back", command=lambda: open_main_application(current_user)).pack(pady=10)

# Main application screen (after login)
def open_main_application(username):
    global current_user
    current_user = username  # Keep track of the logged-in user

    # Clear window and display main app content
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f"Welcome, {username}!").pack(pady=10)

    # Buttons for main features
    tk.Button(root, text="View Books", command=open_book_listing).pack(pady=10)
    tk.Button(root, text="Add Book", command=open_add_book_window).pack(pady=10)
    tk.Label(root, text="Search Books").pack(pady=10)
    global search_entry
    search_entry = tk.Entry(root)
    search_entry.pack(pady=5)
    tk.Button(root, text="Search", command=open_search_results).pack(pady=5)
    tk.Button(root, text="Logout", command=open_login_screen).pack(pady=10)

# Add a book (simple form)
def open_add_book_window():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Add a Book").pack(pady=10)
    tk.Label(root, text="Title").pack()
    title_entry = tk.Entry(root)
    title_entry.pack(pady=5)
    tk.Label(root, text="Genre").pack()
    genre_entry = tk.Entry(root)
    genre_entry.pack(pady=5)

    def submit_book():
        title = title_entry.get()
        genre = genre_entry.get()
        if title and genre:
            add_book(title, genre)
            open_main_application(current_user)

    tk.Button(root, text="Add Book", command=submit_book).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: open_main_application(current_user)).pack(pady=10)

# Registration screen
def open_register_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Register").pack(pady=10)
    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)
    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    def submit_registration():
        username = username_entry.get()
        password = password_entry.get()
        if username and password:
            register_user(username, password)

    tk.Button(root, text="Register", command=submit_registration).pack(pady=10)
    tk.Button(root, text="Back to Login", command=open_login_screen).pack(pady=10)

# Login screen
def open_login_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Login").pack(pady=10)
    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)
    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    def submit_login():
        username = username_entry.get()
        password = password_entry.get()
        if username and password:
            login_user(username, password)

    tk.Button(root, text="Login", command=submit_login).pack(pady=10)
    tk.Button(root, text="Register", command=open_register_screen).pack(pady=10)

# Main GUI setup
root = tk.Tk()
root.title("Book Exchange Platform for Wilkes University")
root.geometry("480x480")  # Window size

# Initial screen: Login
open_login_screen()

root.mainloop()
