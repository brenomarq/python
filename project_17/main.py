from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [
    Question(question['text'], question['answer'])
    for question in question_data
]

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    answer = quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
