from random import randint

#how many tries user have did
tries = 3

while tries > 0:
    print("Rock ( 1 ) , Paper ( 2 ) , Scissor ( 3 )")

    # take user input
    userInput = int(input(": "))

    randomNumber = randint(1,3)

    arr = [0 , "Rock", "Paper", "Scissor"]

    print(f"You: {arr[userInput]}")

    if randomNumber == 1: # computer has chosen rock
        print(f"Computer: Rock !")
        if userInput == 2:
            tries += 1
            print(f"You win this time now you have {str(tries)} left")
        else:
            if userInput == randomNumber:
                continue
            else:
                tries = tries - 1
                print(f"You lose this time now you have {str(tries)} left")
                continue

    elif randomNumber == 2: # computer has chosen paper
        print(f"Computer: Paper !")
        if userInput == 3:
            tries += 1
            print(f"You win this time now you have {str(tries)} left")
        else:
            if userInput == randomNumber:
                print(f"Both choose same so we are skipping this one")
                continue
            else:
                tries = tries - 1
                print(f"You lose this time now you have {str(tries)} left")
                continue

    elif randomNumber == 3: # computer has chosen Scissor
        print(f"Computer: Scissor !")
        if userInput == 1:
            tries += 1
            print(f"You win this time now you have {str(tries)} left")
        else:
            if userInput == randomNumber:
                print(f"Both choose same so we are skipping this one")
                continue
            else:
                tries = tries - 1
                print(f"You lose this time now you have {str(tries)} left")
                continue

