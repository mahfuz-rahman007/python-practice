# This is a guessing number game
import random

randomNumber = random.randint(1, 50)

def main():
    print("Hi whats your name?")
    name = input()
    print("Hi " + name + " ! Lets Play a game. Can You guess a Number between 1 to 50? Remember You have 5 Tries")

    numberOfTies = 5

    while numberOfTies > 0:
        inputNumber = input()
        numberOfTies -= 1

        try:
            if int(inputNumber) > randomNumber:
                print("You Guess To High !! " + str(numberOfTies)  + " Tries Left")

            elif int(inputNumber) < randomNumber:
                print("You Guess is Too Low " + str(numberOfTies) + " Tries Left")

            else: 
                print("Congratulations You Guessed it!!")
                return
        except:
            print("Please Enter a Valid Number")
            numberOfTies = 5

    print("Sad!! You couldn't get it guessed it right, It was " + str(randomNumber))


main()