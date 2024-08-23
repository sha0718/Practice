print("welcome to my game")
playing = input("do you want to play? ")
if playing.lower() != "yes":
    quit()
print("okay! Lets play :)")
score = 0 
answer = input("what does CPU stands for? ")  
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does IPS stands for? ")  
if answer.lower() == "indian police service":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does IRS stands for? ")  
if answer.lower() == "indian revenue services":
    print("correct!")
    score += 1
else:
    print("incorrect!")


answer = input("what does GPU stands for? ")  
if answer.lower() == "graphic processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does APU stands for? ")  
if answer.lower() == "another processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")
print("You got " + str(score) + "question correct!")
print("You got " + str((score / 5) *100) +"%.")    