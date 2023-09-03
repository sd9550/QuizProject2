import tkinter
import quiz_data
from quiz_data import QUIZ_LIMIT
from functools import partial

FONT_NAME = "Arial"


class UI:

    def __init__(self):
        self.qd = quiz_data.QuizData()
        self.score = 0
        self.window = tkinter.Tk()
        self.window.grid()
        self.window.title("Quiz Project")
        self.window.config(padx=50, pady=20, bg="#d6eaf8")
        self.question_text = tkinter.Label(text="Placeholder question text.", font=(FONT_NAME, 10, "bold"), wraplength=500)
        self.score_text = tkinter.Label(text="0/10", font=(FONT_NAME, 10, "bold"))
        self.first_button = tkinter.Button(text="One - placeholder text", font=(FONT_NAME, 10, "bold"), bg="black",
                                           fg="white",
                                           command=partial(self.answer_question, 0))
        self.second_button = tkinter.Button(text="Two - placeholder text", font=(FONT_NAME, 10, "bold"), bg="black",
                                            fg="white",
                                            command=partial(self.answer_question, 1))
        self.third_button = tkinter.Button(text="Three - placeholder text", font=(FONT_NAME, 10, "bold"), bg="black",
                                           fg="white",
                                           command=partial(self.answer_question, 2))
        self.fourth_button = tkinter.Button(text="Four - placeholder text", font=(FONT_NAME, 10, "bold"), bg="black",
                                            fg="white",
                                            command=partial(self.answer_question, 3))
        self.question_text.grid(column=0, row=0, pady=15)
        self.first_button.grid(column=0, row=1, pady=15)
        self.second_button.grid(column=0, row=2, pady=15)
        self.third_button.grid(column=0, row=3, pady=15)
        self.fourth_button.grid(column=0, row=4, pady=15)
        self.score_text.grid(column=0, row=5, pady=25)
        self.get_questions_answers()

    def get_questions_answers(self):
        if self.qd.quiz_over:
            self.first_button.destroy()
            self.second_button.destroy()
            self.third_button.destroy()
            self.fourth_button.destroy()
            self.question_text.config(text="Quiz is over")
        else:
            current_question = self.qd.question
            first_answer = self.qd.answers[0]
            second_answer = self.qd.answers[1]
            third_answer = self.qd.answers[2]
            fourth_answer = self.qd.answers[3]
            self.question_text.config(text=current_question)
            self.first_button.config(text=first_answer)
            self.second_button.config(text=second_answer)
            self.third_button.config(text=third_answer)
            self.fourth_button.config(text=fourth_answer)

    def answer_question(self, index):
        if self.qd.correct_answer == self.qd.answers[index]:
            self.score += 1
            self.score_text.config(text=f"{self.score}/{QUIZ_LIMIT}")
        self.qd.setup_quiz()
        self.get_questions_answers()
