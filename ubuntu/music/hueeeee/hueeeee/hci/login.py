from tkinter import *
from tkinter import messagebox

# ------------------ MAIN WINDOW ------------------
root = Tk()
root.title("Student Registration Portal")
root.geometry("400x400")
root.config(bg="#f5f6fa")

# ------------------ FUNCTIONS ------------------
def show_login_page():
    clear_window()
    Label(root, text="Login Page", font=("Arial", 16, "bold"), bg="#f5f6fa").pack(pady=15)

    Label(root, text="Username:", bg="#f5f6fa", font=("Arial", 12)).pack()
    username_entry = Entry(root, width=25, font=("Arial", 12))
    username_entry.pack(pady=5)

    Label(root, text="Password:", bg="#f5f6fa", font=("Arial", 12)).pack()
    password_entry = Entry(root, width=25, font=("Arial", 12), show="*")
    password_entry.pack(pady=5)

    def next_to_personal():
        user = username_entry.get()
        pwd = password_entry.get()
        if user == "" or pwd == "":
            messagebox.showwarning("Warning", "Please fill all fields!")
        else:
            show_personal_page(user)

    Button(root, text="Next", bg="#0984e3", fg="white", width=10, font=("Arial", 11), command=next_to_personal).pack(pady=15)


def show_personal_page(username):
    clear_window()
    Label(root, text=f"Personal Information", font=("Arial", 16, "bold"), bg="#f5f6fa").pack(pady=15)
    Label(root, text=f"Welcome, {username}", font=("Arial", 12), bg="#f5f6fa", fg="#636e72").pack(pady=5)

    Label(root, text="Full Name:", bg="#f5f6fa", font=("Arial", 12)).pack()
    name_entry = Entry(root, width=30)
    name_entry.pack(pady=5)

    Label(root, text="Email ID:", bg="#f5f6fa", font=("Arial", 12)).pack()
    email_entry = Entry(root, width=30)
    email_entry.pack(pady=5)

    Label(root, text="Contact No.:", bg="#f5f6fa", font=("Arial", 12)).pack()
    contact_entry = Entry(root, width=30)
    contact_entry.pack(pady=5)

    def next_to_academic():
        if name_entry.get() == "" or email_entry.get() == "" or contact_entry.get() == "":
            messagebox.showwarning("Warning", "Please fill all fields!")
        else:
            show_academic_page(username, name_entry.get(), email_entry.get(), contact_entry.get())

    Button(root, text="Next", bg="#00b894", fg="white", width=10, font=("Arial", 11), command=next_to_academic).pack(pady=15)
    Button(root, text="Back", bg="#b2bec3", width=10, font=("Arial", 11), command=show_login_page).pack()


def show_academic_page(username, name, email, contact):
    clear_window()
    Label(root, text="Academic Information", font=("Arial", 16, "bold"), bg="#f5f6fa").pack(pady=15)

    Label(root, text="Course:", bg="#f5f6fa", font=("Arial", 12)).pack()
    course_entry = Entry(root, width=30)
    course_entry.pack(pady=5)

    Label(root, text="Year:", bg="#f5f6fa", font=("Arial", 12)).pack()
    year_entry = Entry(root, width=30)
    year_entry.pack(pady=5)

    Label(root, text="CGPA / Percentage:", bg="#f5f6fa", font=("Arial", 12)).pack()
    cgpa_entry = Entry(root, width=30)
    cgpa_entry.pack(pady=5)

    def submit_form():
        if course_entry.get() == "" or year_entry.get() == "" or cgpa_entry.get() == "":
            messagebox.showwarning("Warning", "Please fill all fields!")
        else:
            messagebox.showinfo("Success", f"Registration Complete!\n\n"
                                           f"Name: {name}\nEmail: {email}\nContact: {contact}\n"
                                           f"Course: {course_entry.get()}\nYear: {year_entry.get()}\nCGPA: {cgpa_entry.get()}")

    Button(root, text="Submit", bg="#6c5ce7", fg="white", width=10, font=("Arial", 11), command=submit_form).pack(pady=15)
    Button(root, text="Back", bg="#b2bec3", width=10, font=("Arial", 11), command=lambda: show_personal_page(username)).pack()

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# ------------------ START APP ------------------
show_login_page()
root.mainloop()
