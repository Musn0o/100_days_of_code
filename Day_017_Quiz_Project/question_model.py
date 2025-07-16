# --- question_model.py ---
# This file defines the Question class.

class Question:
    def __init__(self, q_text, q_answer):
        """
        Initializes a Question object.
        :param q_text: The text of the question.
        :param q_answer: The correct answer to the question (True/False).
        """
        self.text = q_text
        self.answer = q_answer
