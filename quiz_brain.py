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

        def next_question(question_text):
            current_question = self.question_list(self.question_number)
            input(
                f'Q. {self.question_number}: {current_question.text} (True/False):')
