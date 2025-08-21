import random

computer=random.choice([-1,0,1])
youstr=input("Enter Your choice: ")
youdict={"G":0,"S":1,"W":-1}
reversedict={0:"GUN",1:"SNAKE",-1:"WATER"}
you=youdict[youstr]

print(f"You choose {reversedict[you]}\nComputer choose {reversedict[computer]}")

if(computer==you):
    print("It's A Draw")

else:
    if((computer-you) == -1 or (computer-you) == 2):
        print("You Lose")
 
    else:
        print("You win")