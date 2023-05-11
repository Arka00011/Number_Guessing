import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            break

guess_number()
