print("Welcome to my computer quiz!!")

playing = input("Do you want to play the quiz? ")

if playing.lower() != 'yes':
    quit()

print("Okay! Let's play :)")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!!")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print("Correct!!")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!!")
    score += 1
else:
    print("Incorrect")

answer = input("What does ROM stands for? ")
if answer.lower() == "read only memory":
    print("Correct!!")
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print("Correct!!")
    score += 1
else:
    print("Incorrect")

print(f"your score is {score} out of 5")

