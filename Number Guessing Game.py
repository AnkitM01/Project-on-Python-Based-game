import random
randNumber=random.randint(1,5)
userGuess=None
guesses=0
# print(randnumber)
while (userGuess != randNumber):
    userGuess=int(input("Enter your guess\n: "))
    guesses += 1
    if (userGuess==randNumber):
        print("You Guessed It Right!")
    else:
        if (userGuess>randNumber):
            print("You Guessed It Wrong! Enter a smaller Number")
        else:
             print("You Guessed It Wrong! Enter a Larger Number")
print(f"You Guessed the number in {guesses} guesses")
with open("Highscore.txt","r") as f:
    Highscore = int(f.read())

if (guesses<Highscore):
    print("You Just Brocken the High Score!")
    with open("Highscore.txt","w") as f:
        f.write(str(guesses))
        
        
