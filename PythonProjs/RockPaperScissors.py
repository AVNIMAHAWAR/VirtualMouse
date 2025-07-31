import random
list =["Rock","Paper","Scissors"]
compChoice = random.choice(list)
# print(compChoice)
while True:
    userChoice = input("Choose Rock Paper or Scissors or Quit(Q):")

    print("User's choice =",userChoice,"\nComp's choice =",compChoice)
    if(userChoice=="Q"):
        break
    if(userChoice==compChoice):
     print("Tie")
      
    elif(userChoice=="Rock"):
        if(compChoice=="Paper"):
            print("Paper covers Rock,You Lose")
        else:
            print("Rock breaks Scissors,You Win")


    elif(userChoice=="Paper"):
        if(compChoice=="Scissors"):
            print("Scissor cuts Paper,You Lose")
        else:
            print("Paper covers Rock,You Win")

    else:
        if(compChoice=="Rock"):
            print("Rock breaks Scissors,You Lose")
        else:
            print("Scissor cuts Paper,You Winn")

print("----GAME OVER----")