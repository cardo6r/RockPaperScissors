import random

options = ["rock","paper","scissors"]
x = random.choice(options)
y = input("Choose rock, paper or scissors:").lower()#just in case they use capital letters
    
#this is used to reject non-conforming answers and only accept the correct ones    
while y not in options:
    y = input("You have entered an invalid choice, try again:").lower()
    continue;
else:    
    print("You chose",y,"and the computer chose",x)

while x == "rock":
    if y == "rock":
        print("It is a draw!")
    elif y == "paper":
        print("You have won!")
    elif y == "scissors":
        print("You have lost!")
    break;

while x == "paper":
    if y == "paper":
        print("It is a draw!")
    elif y == "scissors":
        print("You have won!")
    elif y == "rock":
        print("You have lost!")
    break;

while x == "scissors":
    if y == "scissors":
        print("It is a draw!")
    elif y == "rock":
        print("You have won!")
    elif y == "paper":
        print("You have lost!")
    break;