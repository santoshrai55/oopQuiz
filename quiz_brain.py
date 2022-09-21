# todo
# asking the questions
# checking if the answer was correct
# checking if we are the end of the quiz

# ATTRIBUTES
# question number = 0
# questions_list

class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist

    def still_has_question(self):
        # total_question = len(self.question_list)
        # q_number = self.question_number
        # if q_number < total_question:

        #     return True
        # else:
        #     return False
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(
            f'Q. {self.question_number}: {current_question.text} (True/False):')
