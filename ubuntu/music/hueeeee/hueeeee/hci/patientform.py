import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    contact = entry_contact.get()
    address = entry_address.get("1.0", "end-1c")
    department = listbox_dept.get(tk.ACTIVE)
    symptoms = []
    if fever_var.get():
        symptoms.append("Fever")
    if cough_var.get():
        symptoms.append("Cough")
    if headache_var.get():
        symptoms.append("Headache")

    if not name or not age or not contact:
        messagebox.showwarning("Incomplete Form", "Please fill in all required fields!")
        return

    info = f"""
    ----- Patient Details -----
    Name: {name}
    Age: {age}
    Gender: {gender}
    Contact: {contact}
    Address: {address}
    Department: {department}
    Symptoms: {', '.join(symptoms) if symptoms else 'None'}
    """
    messagebox.showinfo("Form Submitted", info)

def reset_form():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    gender_var.set("Male")
    entry_contact.delete(0, tk.END)
    entry_address.delete("1.0", tk.END)
    fever_var.set(False)
    cough_var.set(False)
    headache_var.set(False)
    listbox_dept.selection_clear(0, tk.END)

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Patient Registration Form")
root.geometry("600x600")
root.config(bg="#f0f8ff")

# ---------------- Title ----------------
title_label = tk.Label(root, text="Hospital Patient Registration Form", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="#003366")
title_label.pack(pady=15)

# ---------------- Personal Information ----------------
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=10)

tk.Label(frame, text="Full Name:", font=("Arial", 12), bg="#f0f8ff").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_name = tk.Entry(frame, font=("Arial", 12), width=30)
entry_name.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Age:", font=("Arial", 12), bg="#f0f8ff").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_age = tk.Entry(frame, font=("Arial", 12), width=10)
entry_age.grid(row=1, column=1, sticky="w", pady=5)

tk.Label(frame, text="Gender:", font=("Arial", 12), bg="#f0f8ff").grid(row=2, column=0, sticky="w", padx=10, pady=5)
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male", bg="#f0f8ff", font=("Arial", 11)).grid(row=2, column=1, sticky="w")
tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female", bg="#f0f8ff", font=("Arial", 11)).grid(row=2, column=1, padx=80, sticky="w")

tk.Label(frame, text="Contact No:", font=("Arial", 12), bg="#f0f8ff").grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_contact = tk.Entry(frame, font=("Arial", 12), width=20)
entry_contact.grid(row=3, column=1, sticky="w", pady=5)

tk.Label(frame, text="Address:", font=("Arial", 12), bg="#f0f8ff").grid(row=4, column=0, sticky="nw", padx=10, pady=5)
entry_address = tk.Text(frame, font=("Arial", 12), width=30, height=3)
entry_address.grid(row=4, column=1, pady=5)

# ---------------- Department Selection ----------------
tk.Label(root, text="Select Department:", font=("Arial", 12), bg="#f0f8ff").pack(anchor="w", padx=40, pady=5)
listbox_dept = tk.Listbox(root, font=("Arial", 12), height=5, selectmode=tk.SINGLE)
for dept in ["Cardiology", "Orthopedics", "Neurology", "Dermatology", "General Medicine", "Pediatrics"]:
    listbox_dept.insert(tk.END, dept)
listbox_dept.pack(padx=40, fill="x")

# ---------------- Symptoms ----------------
tk.Label(root, text="Symptoms:", font=("Arial", 12), bg="#f0f8ff").pack(anchor="w", padx=40, pady=5)
fever_var = tk.BooleanVar()
cough_var = tk.BooleanVar()
headache_var = tk.BooleanVar()

tk.Checkbutton(root, text="Fever", variable=fever_var, bg="#f0f8ff", font=("Arial", 11)).pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Cough", variable=cough_var, bg="#f0f8ff", font=("Arial", 11)).pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Headache", variable=headache_var, bg="#f0f8ff", font=("Arial", 11)).pack(anchor="w", padx=60)

# ---------------- Buttons ----------------
btn_frame = tk.Frame(root, bg="#f0f8ff")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Submit", command=submit_form, bg="#4CAF50", fg="white", font=("Arial", 12), width=12).grid(row=0, column=0, padx=20)
tk.Button(btn_frame, text="Reset", command=reset_form, bg="#f44336", fg="white", font=("Arial", 12), width=12).grid(row=0, column=1, padx=20)

# ---------------- Footer ----------------
footer = tk.Label(root, text="© 2025 CityCare Hospital | All Rights Reserved", font=("Arial", 9), bg="#f0f8ff", fg="#555")
footer.pack(side="bottom", pady=10)

root.mainloop()
