# 사용자에게 질문하고, 답이 맞는지 확인하고, 퀴즈를 다 했는지 확인
# 속성은 question_number = 0, question_list가 필요하다.
# 메소드는 next_question()이 필요하다.
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q: {self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, correct_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("정답입니다!")
        else:
            print("틀렸습니다!")
        print(f"정답은: {correct_answer} 입니다.")
        print(f"현재 점수는: {self.score}/{self.question_number}입니다.")
        print("\n")
