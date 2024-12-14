import random

number=random.randrange(10)
totalChances=3
chanceCount=1
while chanceCount<=3 :
    guessedNumber=int(input('Dude..!\nGuess a number..! '))
    chanceCount+=1
    if guessedNumber==number:
        print("Congratulations..! Your guess was right..!")
        break
    elif chanceCount>totalChances and guessedNumber!=number:
        print("OOPS......Better luck next time, my friend..!")
    elif guessedNumber>number:
        print("Your guess is higher")
    else:
        print("Your guess is lower")