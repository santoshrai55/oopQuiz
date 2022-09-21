from question_model import Question
from data import question_data
questionbank = []

for item in question_data:
    question = Question(item['text'], item['answer'])
    questionbank.append(question)

print(questionbank[0].answer)
