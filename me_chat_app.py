import tkinter as tk
from tkinter import messagebox


class ChatApp:
    def __init__(self, backend):
        self.backend = backend
        self.window = tk.Tk()
        self.window.title("Chat App")
        self.current_user = None

        self.login_frame = self.create_login_frame()
        self.chat_frame = self.create_chat_frame()

    def create_login_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(padx=300, pady=300)

        self.username_entry = tk.Entry(frame)
        tk.Label(frame, text="felhasználónév").pack()
        self.username_entry.pack()

        self.password_entry = tk.Entry(frame, show="*")
        tk.Label(frame, text="Jelszó").pack()
        self.password_entry.pack()

        self.register_button = tk.Button(frame, text="Register", command=self.register)
        self.register_button.pack(pady=5)

        self.login_button = tk.Button(frame, text="Login", command=self.login)
        self.login_button.pack(pady=5)

        return frame

    def create_chat_frame(self):
        frame = tk.Frame(self.window)

        self.message_listbox = tk.Listbox(frame, height=10, width=50)
        self.message_listbox.pack(padx=10, pady=10)

        self.message_entry = tk.Entry(frame)
        self.message_entry.pack()

        self.save_button = tk.Button(frame, text="Save Message", command=self.save_message)
        self.save_button.pack(pady=5)

        self.delete_button = tk.Button(frame, text="Delete Message", command=self.delete_message)
        self.delete_button.pack(pady=5)

        self.logout_button = tk.Button(frame, text="Logout", command=self.logout)
        self.logout_button.pack(pady=5)

        return frame

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            # Ellenőrizzük, hogy létezik-e már a felhasználó
            if self.backend.register(username, password):
                messagebox.showinfo("Success", "Registration successful")
            else:
                messagebox.showerror("Error", "Username already exists. Please choose a different one.")
        else:
            messagebox.showerror("Error", "Please provide both username and password")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.backend.login(username, password):
            self.current_user = username
            self.login_frame.pack_forget()
            self.chat_frame.pack(padx=10, pady=10)
            self.load_messages()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def load_messages(self):
        messages = self.backend.get_messages()
        self.message_listbox.delete(0, tk.END)
        for message in messages:
            self.message_listbox.insert(tk.END, message)

    def save_message(self):
        if self.current_user:
            message = self.message_entry.get()
            if message:
                self.backend.save_message(self.current_user, message)
                self.load_messages()
                self.message_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Message cannot be empty")
        else:
            messagebox.showerror("Error", "You must be logged in")

    def delete_message(self):
        selected_index = self.message_listbox.curselection()
        if selected_index:
            message_line = selected_index[0]
            self.backend.delete_message(message_line)
            self.load_messages()
        else:
            messagebox.showerror("Error", "Please select a message to delete")

    def logout(self):
        self.current_user = None
        self.chat_frame.pack_forget()
        self.login_frame.pack(padx=300, pady=300)

    def run(self):
        self.window.mainloop()