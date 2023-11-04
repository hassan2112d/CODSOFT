print( "\nWelcome to Quiz: \n")

questions = (
    "What is the line is called which passes through to the center of the earth? : \n",
    "Which planet is the hottest in the solar system ? : \n",
    "How many bones are in the human body? : \n",
    "How many legs does duck have? : \n",
    "What is the capital of Pakistan ? : \n"
    )
options = (("A. Latitude ","B. Longitude ", "C. Equator","D. Aithtic Line \n"),
           ("A. Mercury " , "B. Mars " , "C. Venus " , "D. Earth \n" ),
           ("A. 208 ","B. 207 ","C. 209" , "D. 206 \n"),
           ("A. 2 " , "B. 6" , "C. 4" , "D. 2 \n"),
           ("A. Karachi","B. Lahore" , "C. Peshawar" , "D. Islamabad \n"))

answers = ("C","C","D","A","D")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A,B,C,D) : ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score +=1
        print("Correct !")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is correct")
    question_num +=1

print("---------------------")
print("   Results   ")
print("---------------------")

print("answers : ", end="" )

for answer in answers:
    print(answer, end="")

print()

print("Guesses : ", end="" )

for guess in guesses:
    print(guess, end="")

print()

score = int(score / len(questions) * 100)

print(f"Your score is {score} %")