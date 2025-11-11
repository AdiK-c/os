import tkinter as tk
from tkinter import messagebox

def open_login():
    messagebox.showinfo("Login", "Redirecting to Login Page...")

def open_register():
    messagebox.showinfo("Register", "Redirecting to Registration Page...")

def exit_app():
    root.destroy()

# Main window
root = tk.Tk()
root.title("Welcome Screen")
root.geometry("500x350")
root.config(bg="#e6f0ff")

# Title label
title = tk.Label(root, text="Welcome to Our Application!", font=("Arial", 18, "bold"), bg="#e6f0ff", fg="#003366")
title.pack(pady=30)

# Subtitle
subtitle = tk.Label(root, text="Your comfort, our priority.", font=("Arial", 12), bg="#e6f0ff", fg="#004080")
subtitle.pack(pady=5)

# Buttons
btn_login = tk.Button(root, text="Login", width=20, font=("Arial", 12), bg="#4CAF50", fg="white", command=open_login)
btn_login.pack(pady=15)

btn_register = tk.Button(root, text="Register", width=20, font=("Arial", 12), bg="#2196F3", fg="white", command=open_register)
btn_register.pack(pady=10)

btn_exit = tk.Button(root, text="Exit", width=20, font=("Arial", 12), bg="#f44336", fg="white", command=exit_app)
btn_exit.pack(pady=15)

# Footer
footer = tk.Label(root, text="Thank you for visiting!", font=("Arial", 10, "italic"), bg="#e6f0ff", fg="#555")
footer.pack(side="bottom", pady=10)

# Run the window
root.mainloop()
