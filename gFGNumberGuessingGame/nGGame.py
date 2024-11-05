# this is a number guessing game
# take two inputs from user a-lower range and b- upper range
# using random function choose a number

# let the user keep guessing some random interger
# limit number of guess to log2(upper bound - lower bound +1)
#import staments
import random as ran
import math as mat

#variable declaration
lr=0
upr=0
chosennumber=0
won=False
guess_count=0
max_guess_count=0


#take lower and upper values
lr = int(input("please enter a lower range"))
upr = int(input("please enter a upper range"))

#choose a random number
chosennumber = ran.randrange(lr, upr)
max_guess_count = mat.ceil(mat.log((upr - lr + 1), 2))
print("you have "+str(max_guess_count)+" guesses")
while (guess_count < max_guess_count) and (won == False):
    guessval = int(input("enter your guess"))
    if guessval == chosennumber:
        won = True
        print("you guessed right")
        guess_count = guess_count + 1
    elif guessval < chosennumber:
        won = False
        print("Try again you guessed low")
        guess_count = guess_count + 1
    else:
        won = False
        print("Try again you guessed high")
        guess_count = guess_count + 1

if won == False and guess_count == max_guess_count:
    print("the choosen number is :" +str(chosennumber))
    print("Better luck next time")
