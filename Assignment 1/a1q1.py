import random

won = False

first_input = input("Give me a max number (higher than 0): ")

try:
    max_number = float(first_input)
except ValueError:
    max_number = 0
    exit

if max_number == 0:
    print("Please input an integer greater than 0.")
    quit
else:
    random_number = random.randint(1, max_number)
    perc50 = random_number * 0.50
    perc10 = random_number * 0.10
    guesses = 0
    guess = 0
    for i in range(1,6):
        if i == 1:
            afternum = "st"
        elif i == 2:
            afternum = "nd"
        elif i == 3:
            afternum = "rd"
        else:
            afternum = "th"
        guess = input("Please give me your "+str(i)+afternum + " guess: ")

        try:
            guess = float(guess)
            guesses = guesses + 1
        except ValueError:
            print("You Lost! \nInput an integer next time.")
            break

        if guess > random_number:
            if guess >= random_number + perc50:
                print("Your guess is WAY TOO HIGH!")
            elif random_number + perc50 <= guess <= random_number + perc10:
                print("Your guess is too high.")
            else:
                print("Your guess is slightly high.")
        elif guess < random_number:
            if guess <= random_number - perc50:
                print("Your guess is WAY TOO LOW!")
            elif random_number - perc50 >= guess >= random_number - perc10:
                print("Your guess is too low.")
            else:
                print("Your guess is slightly low.")
        elif guess == random_number:
            print("You win! \nThe random number was " + str(random_number) + "! \nYou took " + str(guesses) + " guess(es)!")
            won = True
            break
    if won != True:
        print("You Lost! \nThe random number was " + str(random_number) + ".")
        exit 