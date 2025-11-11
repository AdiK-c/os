from tkinter import *
from tkinter import messagebox

# Function to handle submit
def submit():
    name = entry_name.get()
    roll = entry_roll.get()
    gender = gender_var.get()
    course = listbox_course.get(ACTIVE)
    hobbies = []
    if hobby1_var.get():
        hobbies.append("Reading")
    if hobby2_var.get():
        hobbies.append("Sports")
    if hobby3_var.get():
        hobbies.append("Music")

    if not name or not roll:
        messagebox.showwarning("Input Error", "Please fill all required fields!")
        return

    msg = f"Name: {name}\nRoll No: {roll}\nGender: {gender}\nCourse: {course}\nHobbies: {', '.join(hobbies)}"
    messagebox.showinfo("Student Details", msg)

# Function to clear all fields
def clear():
    entry_name.delete(0, END)
    entry_roll.delete(0, END)
    gender_var.set("Male")
    listbox_course.selection_clear(0, END)
    hobby1_var.set(0)
    hobby2_var.set(0)
    hobby3_var.set(0)

# Main Window
root = Tk()
root.title("Student Registration Form")
root.geometry("450x500")
root.config(bg="#F5F5F5")

# Title Label
Label(root, text="Student Registration Form", font=("Arial", 16, "bold"), bg="#7d2ae8", fg="white", pady=10).pack(fill="x")

# Frame for Form
frame = Frame(root, bg="#F5F5F5")
frame.pack(pady=20)

# Name
Label(frame, text="Full Name:", font=("Arial", 12), bg="#F5F5F5").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_name = Entry(frame, font=("Arial", 12), width=25)
entry_name.grid(row=0, column=1, pady=5)

# Roll Number
Label(frame, text="Roll No:", font=("Arial", 12), bg="#F5F5F5").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_roll = Entry(frame, font=("Arial", 12), width=25)
entry_roll.grid(row=1, column=1, pady=5)

# Gender
Label(frame, text="Gender:", font=("Arial", 12), bg="#F5F5F5").grid(row=2, column=0, sticky="w", padx=10, pady=5)
gender_var = StringVar(value="Male")
Radiobutton(frame, text="Male", variable=gender_var, value="Male", bg="#F5F5F5", font=("Arial", 11)).grid(row=2, column=1, sticky="w")
Radiobutton(frame, text="Female", variable=gender_var, value="Female", bg="#F5F5F5", font=("Arial", 11)).grid(row=2, column=1, padx=80, sticky="w")

# Course Listbox
Label(frame, text="Course:", font=("Arial", 12), bg="#F5F5F5").grid(row=3, column=0, sticky="w", padx=10, pady=5)
listbox_course = Listbox(frame, height=4, selectmode=SINGLE, font=("Arial", 11))
courses = ["B.Tech", "BCA", "B.Sc", "MBA", "MCA"]
for c in courses:
    listbox_course.insert(END, c)
listbox_course.grid(row=3, column=1, pady=5)

# Hobbies
Label(frame, text="Hobbies:", font=("Arial", 12), bg="#F5F5F5").grid(row=4, column=0, sticky="w", padx=10, pady=5)
hobby1_var = IntVar()
hobby2_var = IntVar()
hobby3_var = IntVar()
Checkbutton(frame, text="Reading", variable=hobby1_var, bg="#F5F5F5", font=("Arial", 11)).grid(row=4, column=1, sticky="w")
Checkbutton(frame, text="Sports", variable=hobby2_var, bg="#F5F5F5", font=("Arial", 11)).grid(row=5, column=1, sticky="w")
Checkbutton(frame, text="Music", variable=hobby3_var, bg="#F5F5F5", font=("Arial", 11)).grid(row=6, column=1, sticky="w")

# Buttons
btn_frame = Frame(root, bg="#F5F5F5")
btn_frame.pack(pady=20)
Button(btn_frame, text="Submit", font=("Arial", 12, "bold"), bg="#7d2ae8", fg="white", width=10, command=submit).grid(row=0, column=0, padx=10)
Button(btn_frame, text="Clear", font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", width=10, command=clear).grid(row=0, column=1, padx=10)

# Run the Application
root.mainloop()
