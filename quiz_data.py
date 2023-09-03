import requests
import numpy as np

QUIZ_LIMIT = 10


class QuizData:

    def __init__(self):
        self.quiz_over = False
        self.questions = []
        self.currentIndex = 0
        self.question = ""
        self.correct_answer = ""
        self.answers = []
        url = "https://the-trivia-api.com/api/questions"
        params = {
            "limit": f'{QUIZ_LIMIT}'
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        for row in data:
            self.questions.append(row)

        self.setup_quiz()

    def setup_quiz(self):
        self.question = self.questions[self.currentIndex]["question"]
        self.correct_answer = self.questions[self.currentIndex]["correctAnswer"]
        self.answers = self.questions[self.currentIndex]["incorrectAnswers"]
        self.answers.append(self.correct_answer)
        np.random.shuffle(self.answers)
        self.currentIndex += 1

        if self.currentIndex == QUIZ_LIMIT:
            self.quiz_over = True
