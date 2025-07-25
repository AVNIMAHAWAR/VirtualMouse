import random
# randNum=random.randint(1,100) #includes 1 n 5
# print(randNum)
target=random.randint(1,100)

while True:
    userChoice=input("guess the target or Quit(Q):")
    if(userChoice == "Q"):
        break
    userChoice=int(userChoice)
    if(userChoice == target):
        print("Success:Correct Guess!!")
        break
    elif(userChoice < target):
        print("Wrong Choice:Your num was too small,take a bigger guess")
    else:
        print("Wrong Choice:Your num was too big,take a smaller guess")

print("----Game Over----")