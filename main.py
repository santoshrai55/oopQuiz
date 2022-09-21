from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


questionbank = []

for item in question_data:
    new_question = Question(item['text'], item['answer'])
    questionbank.append(new_question)


quiz = QuizBrain(questionbank)
quiz.next_question()
