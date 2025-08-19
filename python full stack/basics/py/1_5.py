name = input("What is your name?\n")
print("\nGood to have you",name,",Welcome to Kaun Banega Crorepati !\n")
questions = [" Who was the first woman to become the Prime Minister of India? \n A) Indira Gandhi \t B) Pratibha Patil \t C) Sushma Swaraj \t D) Sarojini Naidu \n", "Which planet in our solar system is known as the Red Planet? \n A) Venus \t B) Saturn \t C) Mars \t D) Jupiter \n","Which Indian city is also known as the City of Joy? \n A) Mumbai \t B) Delhi \tC) Jaipur \t D) Kolkata \n", " Which monument in India was built by Shah Jahan in memory of his wife Mumtaz Mahal? \n A) Qutub Minar \t B) Red Fort \t C) Taj Mahal \t D) India Gate \n","Which is the largest animal on Earth? \n A) Elephant \t B) Blue Whale \t C) Giraffe \t D) Great White Shark \n"]
answers = ["A","C","D","C","B"]
a = 1000
b = 2000
c = 3000
d = 4000
e = 5000
answers1 = input(questions[0])
if answers1.upper() == answers[0]:
    print("Correct answer. You have won", a, "INR\n")
    answer2 = input(questions[1])
    if answer2.upper() == answers[1]:
        print("Correct answer. You have won", b, "INR\n")
        answer3 = input(questions[2])
        if answer3.upper() == answers[2]:
            print("Correct answer. You have won", c, "INR\n") 
            answer4 = input(questions[3])
            if answer4.upper() == answers[3]:
                print("Correct answer. You have won", d, "INR\n")
                answer5=input(questions[4])
                if answer5.upper() == answers[4]:
                    print("Correct answer. You have won",e,"INR\n")
                else:
                    print("Wrong answer.You take home amount is",d,"INR\n")
            else:
                print("Wrong answer.You take home amount is",c,"INR\n")
        else:
            print("Wrong answer.You take home amount is",b,"INR\n") 
    else:
        print("Wrong answer.You take home amount is",a,"INR\n")
else:
    print("Better Luck Next Time. Wrong Answer\n")
    
print("It was great playing with you",name)