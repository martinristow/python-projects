class QuizBrain:
    def __init__(self, q_question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_question_list

    def still_had_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.question_number += 1
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False):")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
            print(f"Your current score is : {self.score}/{self.question_number}")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}.")
        print()

