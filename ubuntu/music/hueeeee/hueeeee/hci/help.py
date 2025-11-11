import tkinter as tk
from tkinter import messagebox

def contact_support():
    messagebox.showinfo("Contact Support", "Email: support@myapp.com\nPhone: +91 9876543210")

def about_app():
    messagebox.showinfo("About App", "This application helps users manage their daily tasks efficiently.\n\nVersion: 1.0.0\nDeveloper: Team MyApp")

# Main window
root = tk.Tk()
root.title("Help - MyApp")
root.geometry("600x400")
root.config(bg="#f2f7ff")

# Title
title_label = tk.Label(root, text="Help & Support", font=("Arial", 20, "bold"), bg="#f2f7ff", fg="#003366")
title_label.pack(pady=20)

# Instructions/Help text
help_text = """
Welcome to the Help Section!

Here you can find assistance on how to use the app:

1. To Login: Click the 'Login' button on the home screen and enter your credentials.
2. To Register: Click 'Sign Up' and fill out all required fields.
3. To Access Features: Navigate through the menu bar to explore app modules.
4. To Exit: Click the 'Exit' button to close the application safely.

If you face any issues, contact support below.
"""

help_label = tk.Label(root, text=help_text, font=("Arial", 11), bg="#f2f7ff", justify="left", anchor="w")
help_label.pack(padx=40, pady=10)

# Buttons
btn_about = tk.Button(root, text="About Application", bg="#4CAF50", fg="white", font=("Arial", 12), width=20, command=about_app)
btn_about.pack(pady=10)

btn_contact = tk.Button(root, text="Contact Support", bg="#2196F3", fg="white", font=("Arial", 12), width=20, command=contact_support)
btn_contact.pack(pady=10)

btn_exit = tk.Button(root, text="Close Help", bg="#f44336", fg="white", font=("Arial", 12), width=20, command=root.destroy)
btn_exit.pack(pady=20)

# Footer
footer = tk.Label(root, text="© 2025 MyApp Team | All Rights Reserved", font=("Arial", 9), bg="#f2f7ff", fg="#555")
footer.pack(side="bottom", pady=10)

root.mainloop()
