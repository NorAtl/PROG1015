import random

def main():
    number_to_guess = random.randint(1,10)
    user_guess = 0
    counter = 0

    while user_guess != number_to_guess:
        counter += 1
        user_guess = int(input("Guess a number from 1 to 100: "))
        if number_to_guess < user_guess:
            print("lower")
        elif number_to_guess > user_guess:
            print("higher")

    print(f"You got it! The number is {number_to_guess}. Number of guesses: {counter}.")

if __name__ == "__main__":
    main()