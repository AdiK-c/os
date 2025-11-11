import tkinter as tk
from tkinter import messagebox, ttk

# Function to handle transfer
def transfer_funds():
    sender = entry_sender.get()
    receiver = entry_receiver.get()
    account_no = entry_account.get()
    amount = entry_amount.get()
    payment_mode = payment_var.get()
    note = entry_note.get("1.0", "end-1c")

    if not sender or not receiver or not account_no or not amount:
        messagebox.showwarning("Incomplete Details", "Please fill all required fields!")
        return

    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid transfer amount.")
        return

    summary = f"""
    ---- Transaction Details ----
    Sender: {sender}
    Receiver: {receiver}
    Account No: {account_no}
    Amount: ₹{amount:.2f}
    Payment Mode: {payment_mode}
    Note: {note if note else "None"}
    """

    messagebox.showinfo("Transaction Successful", summary)
    reset_fields()

# Function to reset form
def reset_fields():
    entry_sender.delete(0, tk.END)
    entry_receiver.delete(0, tk.END)
    entry_account.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    payment_var.set("UPI")
    entry_note.delete("1.0", tk.END)

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Fund Transfer / Transaction Window")
root.geometry("600x600")
root.config(bg="#e8f4f8")

# ---------------- Title ----------------
title = tk.Label(root, text="💸 Fund Transfer Portal", font=("Arial", 18, "bold"), bg="#e8f4f8", fg="#004d66")
title.pack(pady=20)

# ---------------- Frame ----------------
frame = tk.Frame(root, bg="#e8f4f8")
frame.pack(padx=30, pady=10)

# Sender Name
tk.Label(frame, text="Sender Name:", font=("Arial", 12), bg="#e8f4f8").grid(row=0, column=0, sticky="w", pady=5)
entry_sender = tk.Entry(frame, font=("Arial", 12), width=30)
entry_sender.grid(row=0, column=1, pady=5)

# Receiver Name
tk.Label(frame, text="Receiver Name:", font=("Arial", 12), bg="#e8f4f8").grid(row=1, column=0, sticky="w", pady=5)
entry_receiver = tk.Entry(frame, font=("Arial", 12), width=30)
entry_receiver.grid(row=1, column=1, pady=5)

# Account Number
tk.Label(frame, text="Receiver Account No:", font=("Arial", 12), bg="#e8f4f8").grid(row=2, column=0, sticky="w", pady=5)
entry_account = tk.Entry(frame, font=("Arial", 12), width=30)
entry_account.grid(row=2, column=1, pady=5)

# Amount
tk.Label(frame, text="Amount (₹):", font=("Arial", 12), bg="#e8f4f8").grid(row=3, column=0, sticky="w", pady=5)
entry_amount = tk.Entry(frame, font=("Arial", 12), width=30)
entry_amount.grid(row=3, column=1, pady=5)

# Payment Mode
tk.Label(frame, text="Payment Mode:", font=("Arial", 12), bg="#e8f4f8").grid(row=4, column=0, sticky="w", pady=5)
payment_var = tk.StringVar(value="UPI")
ttk.Combobox(frame, textvariable=payment_var, values=["UPI", "Net Banking", "Credit Card", "Debit Card"], font=("Arial", 12), width=28).grid(row=4, column=1, pady=5)

# Transaction Note
tk.Label(frame, text="Transaction Note:", font=("Arial", 12), bg="#e8f4f8").grid(row=5, column=0, sticky="nw", pady=5)
entry_note = tk.Text(frame, font=("Arial", 12), width=30, height=4)
entry_note.grid(row=5, column=1, pady=5)

# ---------------- Buttons ----------------
btn_frame = tk.Frame(root, bg="#e8f4f8")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Transfer", command=transfer_funds, bg="#009688", fg="white", font=("Arial", 12, "bold"), width=12).grid(row=0, column=0, padx=20)
tk.Button(btn_frame, text="Reset", command=reset_fields, bg="#f44336", fg="white", font=("Arial", 12, "bold"), width=12).grid(row=0, column=1, padx=20)

# ---------------- Footer ----------------
footer = tk.Label(root, text="© 2025 SafeBank | Secure Fund Transfer System", bg="#e8f4f8", fg="#555", font=("Arial", 9))
footer.pack(side="bottom", pady=10)

root.mainloop()
