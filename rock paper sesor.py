
import random
options=["rock","paper","scissors"]
computer=random.choice(options)   #choice of function of this module
user=input("enter your Choices:")

if(user==computer):
    print("it is tie")
else:
    if (user=="rock"):
        if(computer=="paper"):
            print("Computer won,because it is chose paper")
        else:
            print("user won beacuse, computer chose",computer)
    elif (user=="paper"):
        if(computer=="rock"):
              print("user won beacuse, computer chose",computer)
        else:
            print("computer won, it chose scissors")
    elif (user=="scissors"):
        if(computer=="rock"):
              print("computer won, it chose rock")
        else:
            print("user won beacuse,computer chose",computer)



