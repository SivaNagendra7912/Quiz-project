from ques_and_ans import question_data
import random


class Quiz:
    def __init__(self):
        self.score = 0

    def get_question_answer(self):
        ques_ans = random.choice(question_data)
        return ques_ans

    def validate(self, ques_ans, user_ans):
        if (ques_ans['answer']).lower() == user_ans:
            return True
        return False

