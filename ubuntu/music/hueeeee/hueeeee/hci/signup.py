import tkinter as tk
from tkinter import messagebox

def signup():
    name = name_entry.get()
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    gender = gender_var.get()
    interests = []

    if reading_var.get():
        interests.append("Reading")
    if sports_var.get():
        interests.append("Sports")
    if music_var.get():
        interests.append("Music")

    # Validation
    if not (name and email and username and password and gender):
        messagebox.showwarning("Incomplete Data", "Please fill all required fields!")
        return

    # Display summary
    info = f"""
    ✅ Sign-Up Successful!

    Name: {name}
    Email: {email}
    Username: {username}
    Gender: {gender}
    Interests: {', '.join(interests) if interests else 'None'}
    """
    messagebox.showinfo("Success", info)

# Create window
root = tk.Tk()
root.title("Sign-Up Window")
root.geometry("500x600")
root.config(bg="#e6e6fa")

# Heading
tk.Label(root, text="Create Your Account", font=("Arial", 20, "bold"), bg="#e6e6fa", fg="#4b0082").pack(pady=20)

# Name
tk.Label(root, text="Full Name:", font=("Arial", 12), bg="#e6e6fa").pack(anchor="w", padx=60)
name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=60, pady=5)

# Email
tk.Label(root, text="Email:", font=("Arial", 12), bg="#e6e6fa").pack(anchor="w", padx=60)
email_entry = tk.Entry(root, width=40)
email_entry.pack(padx=60, pady=5)

# Username
tk.Label(root, text="Username:", font=("Arial", 12), bg="#e6e6fa").pack(anchor="w", padx=60)
username_entry = tk.Entry(root, width=40)
username_entry.pack(padx=60, pady=5)

# Password
tk.Label(root, text="Password:", font=("Arial", 12), bg="#e6e6fa").pack(anchor="w", padx=60)
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack(padx=60, pady=5)

# Gender
tk.Label(root, text="Gender:", font=("Arial", 12), bg="#e6e6fa").pack(anchor="w", padx=60)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", bg="#e6e6fa").pack(anchor="w", padx=80)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", bg="#e6e6fa").pack(anchor="w", padx=80)
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other", bg="#e6e6fa").pack(anchor="w", padx=80)

# Interests
tk.Label(root, text="Interests:", font=("Arial", 12), bg="#e6e6fa").pack(anchor="w", padx=60)
reading_var = tk.BooleanVar()
sports_var = tk.BooleanVar()
music_var = tk.BooleanVar()

tk.Checkbutton(root, text="Reading", variable=reading_var, bg="#e6e6fa").pack(anchor="w", padx=80)
tk.Checkbutton(root, text="Sports", variable=sports_var, bg="#e6e6fa").pack(anchor="w", padx=80)
tk.Checkbutton(root, text="Music", variable=music_var, bg="#e6e6fa").pack(anchor="w", padx=80)

# Submit button
tk.Button(root, text="Sign Up", command=signup, bg="#4b0082", fg="white", font=("Arial", 12, "bold")).pack(pady=30)

root.mainloop()
