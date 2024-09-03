from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for dictionary in question_data:
    question_text=dictionary["text"]
    answer_text=dictionary["answer"]
    new_q=Question(question_text,answer_text)
    question_bank.append(new_q)

quiz=QuizBrain(question_bank)
while quiz.still_have_questions():
    quiz.next_question()
    
