from quiz import Quiz
print("\nWelcome to National Level Quiz")
print("You have 10 questions in the quiz")
quiz_mania = Quiz()
no_of_ques = 0
correct = 0
for _ in range(10):
    no_of_ques += 1
    print("\nHere is your question")
    ques_ans = quiz_mania.get_question_answer()
    print(ques_ans['text'])
    user_ans = input("(True/ False): ").lower()
    if quiz_mania.validate(ques_ans, user_ans):
        correct += 1
        print("Your answer is correct")
    else:
        print("Your answer is wrong")
    print(f"Your current score is {correct}/{no_of_ques}")
print("\nQuiz is Ended")
print(f"Your final score is {correct}/10")
