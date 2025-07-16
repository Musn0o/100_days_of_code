# --- quiz_brain.py ---
# This file defines the QuizBrain class, which manages the quiz logic.

class QuizBrain:
    def __init__(self, q_list):
        """
        Initializes a QuizBrain object.
        :param q_list: A list of Question objects.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        """
        Checks if there are more questions in the quiz.
        :return: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Retrieves the next question from the question list,
        increments the question number, and prompts the user for an answer.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").lower()
        self.check_answer(user_answer, current_question.answer.lower())

    def check_answer(self, user_answer, correct_answer):
        """
        Checks if the user's answer is correct and updates the score.
        :param user_answer: The answer provided by the user.
        :param correct_answer: The correct answer to the question.
        """
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer.title()}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
