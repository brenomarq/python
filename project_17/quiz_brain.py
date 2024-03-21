class QuizBrain:
    def __init__(self, questions) -> None:
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"\nQ.{self.question_number} {current_question.text}. (True, False)? ")
        self.check_answer(answer, current_question.answer)

    def check_score(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
