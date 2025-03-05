from errno import EWOULDBLOCK
from tkinter import *
from turtle import bgcolor
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
PATH = "Day_34"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("arial", 10, "bold"))
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question = self.canvas.create_text(150, 125, text="Amazon acquired Twitch in August 2024 for $970 million dollars", font=("Arial", 20, "italic"), width=250)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        false_img = PhotoImage(file=f"{PATH}/images/false.png")
        self.button_false = Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.button_false.grid(row=2, column=0)
        true_img = PhotoImage(file=f"{PATH}/images/true.png")
        self.button_true = Button(image=true_img, highlightthickness=0, command=self.answer_true)
        self.button_true.grid(row=2, column=1)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            new_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=new_question)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)