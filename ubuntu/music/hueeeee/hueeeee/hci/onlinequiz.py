import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Quiz")
        self.root.geometry("600x400")
        self.root.config(bg="#e6e6fa")

        self.q_no = 0
        self.score = 0

        # Questions, Options and Answers
        self.questions = [
            "Which language is used for AI?",
            "Which of the following is not an OOP concept?",
            "Which keyword is used to define a function in Python?",
            "What does HTML stand for?",
            "Which protocol is used to send emails?"
        ]

        self.options = [
            ["Python", "C", "Java", "HTML"],
            ["Inheritance", "Encapsulation", "Polymorphism", "Compilation"],
            ["def", "function", "fun", "lambda"],
            ["Hyper Text Markup Language", "HighText Machine Language", "Hyperloop Machine Language", "None of these"],
            ["SMTP", "HTTP", "FTP", "IP"]
        ]

        self.answers = [0, 3, 0, 0, 0]  # correct options (0-based index)

        # Tkinter variables
        self.opt_selected = tk.IntVar()

        # GUI Components
        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.title = tk.Label(self.root, text="Online Quiz System", font=("Arial", 20, "bold"), bg="#e6e6fa", fg="#4b0082")
        self.title.pack(pady=20)

        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=500, bg="#e6e6fa")
        self.question_label.pack(pady=10)

        self.radio_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self.root, text="", variable=self.opt_selected, value=i,
                                 font=("Arial", 12), bg="#e6e6fa", anchor="w")
            btn.pack(fill="x", padx=60, pady=5)
            self.radio_buttons.append(btn)

        self.next_btn = tk.Button(self.root, text="Next", command=self.next_question,
                                  bg="#4b0082", fg="white", font=("Arial", 12, "bold"))
        self.next_btn.pack(pady=20)

    def display_question(self):
        """Display current question and options"""
        self.opt_selected.set(-1)
        self.question_label.config(text=f"Q{self.q_no + 1}: {self.questions[self.q_no]}")

        for i in range(4):
            self.radio_buttons[i].config(text=self.options[self.q_no][i])

    def next_question(self):
        """Check answer and go to next question"""
        if self.opt_selected.get() == self.answers[self.q_no]:
            self.score += 1

        self.q_no += 1
        if self.q_no == len(self.questions):
            self.show_result()
        else:
            self.display_question()

    def show_result(self):
        """Display final result"""
        result = f"Your Score: {self.score} / {len(self.questions)}"
        messagebox.showinfo("Result", result)
        self.root.destroy()

# Run the quiz
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
