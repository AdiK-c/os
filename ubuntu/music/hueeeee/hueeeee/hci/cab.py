import tkinter as tk
from tkinter import messagebox

def confirm_booking():
    name = name_entry.get()
    phone = phone_entry.get()
    pickup = pickup_entry.get()
    drop = drop_entry.get()
    cab_type = cab_var.get()
    payment_mode = payment_var.get()
    extras = []
    if ac_var.get():
        extras.append("AC")
    if music_var.get():
        extras.append("Music")
    if luggage_var.get():
        extras.append("Luggage Support")
    
    if not (name and phone and pickup and drop and cab_type and payment_mode):
        messagebox.showwarning("Incomplete Details", "Please fill all fields before booking!")
        return
    
    summary = f"""
🚗 Booking Confirmed!

Name: {name}
Phone: {phone}
Pickup: {pickup}
Drop: {drop}
Cab Type: {cab_type}
Payment Mode: {payment_mode}
Extra Services: {', '.join(extras) if extras else 'None'}

Thank you for choosing SmartRide! 🌟
    """
    messagebox.showinfo("Booking Successful", summary)

# Create main window
root = tk.Tk()
root.title("SmartRide - Cab/Auto Booking App")
root.geometry("600x750")
root.config(bg="#E6F7FF")

# Heading
tk.Label(root, text="🚖 SmartRide Booking App", font=("Arial", 20, "bold"), bg="#E6F7FF", fg="#003366").pack(pady=20)

# Customer Details
tk.Label(root, text="Customer Name:", font=("Arial", 12), bg="#E6F7FF").pack(anchor="w", padx=80)
name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=80, pady=5)

tk.Label(root, text="Phone Number:", font=("Arial", 12), bg="#E6F7FF").pack(anchor="w", padx=80)
phone_entry = tk.Entry(root, width=40)
phone_entry.pack(padx=80, pady=5)

# Pickup and Drop Info
tk.Label(root, text="Pickup Location:", font=("Arial", 12), bg="#E6F7FF").pack(anchor="w", padx=80)
pickup_entry = tk.Entry(root, width=40)
pickup_entry.pack(padx=80, pady=5)

tk.Label(root, text="Drop Location:", font=("Arial", 12), bg="#E6F7FF").pack(anchor="w", padx=80)
drop_entry = tk.Entry(root, width=40)
drop_entry.pack(padx=80, pady=5)

# Cab Type
tk.Label(root, text="Select Vehicle Type:", font=("Arial", 12), bg="#E6F7FF").pack(anchor="w", padx=80)
cab_var = tk.StringVar(value="Auto")
tk.Radiobutton(root, text="Auto", variable=cab_var, value="Auto", bg="#E6F7FF").pack(anchor="w", padx=100)
tk.Radiobutton(root, text="Mini Cab", variable=cab_var, value="Mini Cab", bg="#E6F7FF").pack(anchor="w", padx=100)
tk.Radiobutton(root, text="Sedan", variable=cab_var, value="Sedan", bg="#E6F7FF").pack(anchor="w", padx=100)
tk.Radiobutton(root, text="SUV", variable=cab_var, value="SUV", bg="#E6F7FF").pack(anchor="w", padx=100)

# Payment Mode
tk.Label(root, text="Select Payment Mode:", font=("Arial", 12), bg="#E6F7FF").pack(anchor="w", padx=80)
payment_var = tk.StringVar()
tk.Radiobutton(root, text="Cash", variable=payment_var, value="Cash", bg="#E6F7FF").pack(anchor="w", padx=100)
tk.Radiobutton(root, text="UPI / Online", variable=payment_var, value="UPI / Online", bg="#E6F7FF").pack(anchor="w", padx=100)

# Extra Features
tk.Label(root, text="Additional Preferences:", font=("Arial", 12), bg="#E6F7FF").pack(anchor="w", padx=80)
ac_var = tk.BooleanVar()
music_var = tk.BooleanVar()
luggage_var = tk.BooleanVar()
tk.Checkbutton(root, text="AC", variable=ac_var, bg="#E6F7FF").pack(anchor="w", padx=100)
tk.Checkbutton(root, text="Music", variable=music_var, bg="#E6F7FF").pack(anchor="w", padx=100)
tk.Checkbutton(root, text="Luggage Support", variable=luggage_var, bg="#E6F7FF").pack(anchor="w", padx=100)

# Submit Button
tk.Button(root, text="Book Now", command=confirm_booking, bg="#003366", fg="white",
          font=("Arial", 13, "bold"), width=20).pack(pady=40)

root.mainloop()
