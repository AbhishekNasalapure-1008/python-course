class QuizBrain():
    def __init__(self,question_list):
        self.questions=question_list
        self.question_number = 0
        self.score = 0

    def still_have_questions(self):
        return self.question_number < len(self.questions)
    

    def next_question(self):
        current_question= self.questions[self.question_number]
        self.question_number += 1
        user_answer=input(f"Q.{self.question_number}: {current_question.question}?  (True/false)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer , currect_answer):
        if user_answer.lower()==currect_answer.lower():
            self.score+=1
            print("Yes, you got it right")
        else:
            print("you got it wrong")

        print(f"Your score={self.score}/{len(self.questions)}")
        print(f"the currect answer was:{currect_answer}\n")






