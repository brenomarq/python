import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.score_label = None
        self.canvas = None
        self.question = None
        self.false_btn = None
        self.true_btn = None
        self.false_icon = None
        self.true_icon = None
        self._set_ui()

        self.window.mainloop()

    def _set_ui(self) -> None:
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", font=("Arial", 13, "normal"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250)
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some random question.",
            fill=THEME_COLOR,
            font=FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.false_icon = tk.PhotoImage(file="./images/false.png")
        self.false_btn = tk.Button(image=self.false_icon, command=self.false_clicked, highlightthickness=0)
        self.false_btn.grid(row=2, column=0)

        self.true_icon = tk.PhotoImage(file="./images/true.png")
        self.true_btn = tk.Button(image=self.true_icon, command=self.true_clicked, highlightthickness=0)
        self.true_btn.grid(row=2, column=1)

        self.get_next_question()

    def false_clicked(self) -> None:
        is_correct = self.quiz.check_answer("false")
        self.give_feedback(is_correct)

        if is_correct:
            self.update_score(self.quiz.score)

    def true_clicked(self) -> None:
        is_correct = self.quiz.check_answer("true")
        self.give_feedback(is_correct)

        if is_correct:
            self.update_score(self.quiz.score)

    def give_feedback(self, is_correct: bool) -> None:
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.canvas.itemconfig(self.question, fill="white")
        self.window.after(1000, self.get_next_question)

    def update_score(self, score: int) -> None:
        self.score_label.config(text=f"Score: {score}")

    def get_next_question(self) -> None:
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question, fill=THEME_COLOR)

        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.false_btn.config(state="disabled")
            self.true_btn.config(state="disabled")
