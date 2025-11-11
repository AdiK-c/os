import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    sport = sport_var.get()
    phone = phone_entry.get()
    email = email_entry.get()

    facilities = []
    if gym_var.get():
        facilities.append("Gym Access")
    if coach_var.get():
        facilities.append("Personal Coaching")
    if diet_var.get():
        facilities.append("Diet Consultation")

    if not (name and age and gender and sport and phone and email):
        messagebox.showwarning("Incomplete Form", "Please fill all required fields!")
        return

    summary = f"""
🏅 Sports Academy Registration Successful!

Name: {name}
Age: {age}
Gender: {gender}
Sport Selected: {sport}
Phone: {phone}
Email: {email}
Facilities Opted: {', '.join(facilities) if facilities else 'None'}

Welcome to the Sports Academy! 🏆
"""
    messagebox.showinfo("Registration Successful", summary)

# Create main window
root = tk.Tk()
root.title("🏅 Sports Academy Registration Form")
root.geometry("600x750")
root.config(bg="#E8F3FF")

# Heading
tk.Label(root, text="Sports Academy Registration Form", font=("Arial", 20, "bold"), bg="#E8F3FF", fg="#003366").pack(pady=20)

# Name
tk.Label(root, text="Full Name:", font=("Arial", 12), bg="#E8F3FF").pack(anchor="w", padx=80)
name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=80, pady=5)

# Age
tk.Label(root, text="Age:", font=("Arial", 12), bg="#E8F3FF").pack(anchor="w", padx=80)
age_entry = tk.Entry(root, width=40)
age_entry.pack(padx=80, pady=5)

# Gender
tk.Label(root, text="Gender:", font=("Arial", 12), bg="#E8F3FF").pack(anchor="w", padx=80)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", bg="#E8F3FF").pack(anchor="w", padx=100)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", bg="#E8F3FF").pack(anchor="w", padx=100)
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other", bg="#E8F3FF").pack(anchor="w", padx=100)

# Sport Selection
tk.Label(root, text="Select Sport:", font=("Arial", 12), bg="#E8F3FF").pack(anchor="w", padx=80)
sport_var = tk.StringVar()
sport_choices = ["Cricket", "Football", "Badminton", "Tennis", "Swimming", "Basketball"]
sport_menu = tk.OptionMenu(root, sport_var, *sport_choices)
sport_menu.config(width=35)
sport_menu.pack(padx=80, pady=5)

# Contact Details
tk.Label(root, text="Phone Number:", font=("Arial", 12), bg="#E8F3FF").pack(anchor="w", padx=80)
phone_entry = tk.Entry(root, width=40)
phone_entry.pack(padx=80, pady=5)

tk.Label(root, text="Email ID:", font=("Arial", 12), bg="#E8F3FF").pack(anchor="w", padx=80)
email_entry = tk.Entry(root, width=40)
email_entry.pack(padx=80, pady=5)

# Facilities
tk.Label(root, text="Additional Facilities:", font=("Arial", 12), bg="#E8F3FF").pack(anchor="w", padx=80)
gym_var = tk.BooleanVar()
coach_var = tk.BooleanVar()
diet_var = tk.BooleanVar()
tk.Checkbutton(root, text="Gym Access", variable=gym_var, bg="#E8F3FF").pack(anchor="w", padx=100)
tk.Checkbutton(root, text="Personal Coaching", variable=coach_var, bg="#E8F3FF").pack(anchor="w", padx=100)
tk.Checkbutton(root, text="Diet Consultation", variable=diet_var, bg="#E8F3FF").pack(anchor="w", padx=100)

# Submit Button
tk.Button(root, text="Register Now", command=submit_form, bg="#003366", fg="white",
          font=("Arial", 13, "bold"), width=20).pack(pady=40)

root.mainloop()
