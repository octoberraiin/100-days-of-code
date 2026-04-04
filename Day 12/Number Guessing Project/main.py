import random
from art import logo

def check_guess(attempts, rand_num):
    while attempts > 0:
        u_guess = int(input("Make a guess: "))

        if u_guess == rand_num:
            print("You guessed the number! You win!")
            return
        elif u_guess < rand_num:
            print("Too low!")
        else:
            print("Too high!")

        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")

    print(f"The number was {rand_num}.")
    print("You ran out of attempts. Refresh the page to play again.")


# The game:
print(logo)
print("Welcome to the Number Guessing Game!")

random_number = random.randint(1, 100)
print(f"Pssst, the correct answer is {random_number}.")

print("I'm thinking of a number between 1 and 100.")
easy_or_hard = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if easy_or_hard == "easy":
    guesses_left = 10
elif easy_or_hard == "hard":
    guesses_left = 5
else:
    print("Error! Please choose a valid difficulty.")
    exit()

print(f"You have {guesses_left} attempts remaining to guess the number.")
check_guess(guesses_left, random_number)
