import tkinter as tk
from tkinter import messagebox

def submit_feedback():
    name = name_entry.get()
    email = email_entry.get()
    food_quality = quality_var.get()
    service = service_var.get()
    cleanliness = clean_var.get()
    suggestions = suggestion_text.get("1.0", "end-1c")

    liked_items = []
    if taste_var.get():
        liked_items.append("Taste")
    if presentation_var.get():
        liked_items.append("Presentation")
    if freshness_var.get():
        liked_items.append("Freshness")

    if not name or not email or not (food_quality and service and cleanliness):
        messagebox.showwarning("Incomplete Form", "Please fill all required fields!")
        return

    summary = f"""
    🍽️ Thank you for your feedback!

    Name: {name}
    Email: {email}
    Food Quality: {food_quality}
    Service: {service}
    Cleanliness: {cleanliness}
    Liked Aspects: {', '.join(liked_items) if liked_items else 'None'}
    Suggestions: {suggestions if suggestions else 'No suggestions provided.'}
    """

    messagebox.showinfo("Feedback Submitted", summary)

# Create main window
root = tk.Tk()
root.title("Hotel Food Feedback Form")
root.geometry("600x700")
root.config(bg="#FFF0F5")

# Heading
tk.Label(root, text="🍴 Customer Feedback Form 🍴", 
         font=("Arial", 20, "bold"), bg="#FFF0F5", fg="#8B0000").pack(pady=20)

# Customer Info
tk.Label(root, text="Name:", font=("Arial", 12), bg="#FFF0F5").pack(anchor="w", padx=80)
name_entry = tk.Entry(root, width=50)
name_entry.pack(padx=80, pady=5)

tk.Label(root, text="Email:", font=("Arial", 12), bg="#FFF0F5").pack(anchor="w", padx=80)
email_entry = tk.Entry(root, width=50)
email_entry.pack(padx=80, pady=5)

# Food Quality Rating
tk.Label(root, text="Food Quality:", font=("Arial", 12), bg="#FFF0F5").pack(anchor="w", padx=80)
quality_var = tk.StringVar()
tk.Radiobutton(root, text="Excellent", variable=quality_var, value="Excellent", bg="#FFF0F5").pack(anchor="w", padx=100)
tk.Radiobutton(root, text="Good", variable=quality_var, value="Good", bg="#FFF0F5").pack(anchor="w", padx=100)
tk.Radiobutton(root, text="Average", variable=quality_var, value="Average", bg="#FFF0F5").pack(anchor="w", padx=100)
tk.Radiobutton(root, text="Poor", variable=quality_var, value="Poor", bg="#FFF0F5").pack(anchor="w", padx=100)

# Service Rating
tk.Label(root, text="Service:", font=("Arial", 12), bg="#FFF0F5").pack(anchor="w", padx=80)
service_var = tk.StringVar()
tk.Radiobutton(root, text="Excellent", variable=service_var, value="Excellent", bg="#FFF0F5").pack(anchor="w", padx=100)
tk.Radiobutton(root, text="Good", variable=service_var, value="Good", bg="#FFF0F5").pack(anchor="w", padx=100)
tk.Radiobutton(root, text="Average", variable=service_var, value="Average", bg="#FFF0F5").pack(anchor="w", padx=100)
tk.Radiobutton(root, text="Poor", variable=service_var, value="Poor", bg="#FFF0F5").pack(anchor="w", padx=100)

# Cleanliness Rating
tk.Label(root, text="Cleanliness:", font=("Arial", 12), bg="#FFF0F5").pack(anchor="w", padx=80)
clean_var = tk.StringVar()
tk.Radiobutton(root, text="Excellent", variable=clean_var, value="Excellent", bg="#FFF0F5").pack(anchor="w", padx=100)
tk.Radiobutton(root, text="Good", variable=clean_var, value="Good", bg="#FFF0F5").pack(anchor="w", padx=100)
tk.Radiobutton(root, text="Average", variable=clean_var, value="Average", bg="#FFF0F5").pack(anchor="w", padx=100)
tk.Radiobutton(root, text="Poor", variable=clean_var, value="Poor", bg="#FFF0F5").pack(anchor="w", padx=100)

# Checkbuttons for liked aspects
tk.Label(root, text="What did you like the most?", font=("Arial", 12), bg="#FFF0F5").pack(anchor="w", padx=80)
taste_var = tk.BooleanVar()
presentation_var = tk.BooleanVar()
freshness_var = tk.BooleanVar()
tk.Checkbutton(root, text="Taste", variable=taste_var, bg="#FFF0F5").pack(anchor="w", padx=100)
tk.Checkbutton(root, text="Presentation", variable=presentation_var, bg="#FFF0F5").pack(anchor="w", padx=100)
tk.Checkbutton(root, text="Freshness", variable=freshness_var, bg="#FFF0F5").pack(anchor="w", padx=100)

# Suggestions
tk.Label(root, text="Suggestions / Comments:", font=("Arial", 12), bg="#FFF0F5").pack(anchor="w", padx=80, pady=(10,0))
suggestion_text = tk.Text(root, width=50, height=5)
suggestion_text.pack(padx=80, pady=5)

# Submit Button
tk.Button(root, text="Submit Feedback", command=submit_feedback, bg="#8B0000", fg="white",
          font=("Arial", 12, "bold")).pack(pady=30)

root.mainloop()
