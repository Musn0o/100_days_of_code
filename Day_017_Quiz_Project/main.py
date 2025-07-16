from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# --- main.py ---
# This is the main script to run the Quiz Project.

# Create a list to store Question objects
question_bank = []
# Populate the question_bank with Question objects from question_data
for question_item in question_data:
    question_text = question_item["text"]
    question_answer = question_item["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create a QuizBrain object, passing the list of Question objects
quiz = QuizBrain(question_bank)

# Loop through the quiz as long as there are questions remaining
while quiz.still_has_questions():
    quiz.next_question()

# Print the final results after the quiz is completed
print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")

