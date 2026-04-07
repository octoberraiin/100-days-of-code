import random
from art import logo
from art import vs
from game_data import data

global choices
global correct

def random_choices(choice1, choice2):
    """ Takes two random choices and prints necessary parts of a random choice """
    while choice1 == choice2:
        choice2 = random.choice(data)
    print(f"Compare A: {choice1['name']}, a {choice1['description']}, from {choice1['country']}.")
    print(vs)
    print(f"Against B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}.")
    global choices
    choices = [choice1, choice2]


def compare_followers(first_choice, second_choice):
    """ Checks and finds correct answer """
    global correct
    if first_choice > second_choice:
        correct = "a"
    elif first_choice < second_choice:
        correct = "b"
    elif first_choice == second_choice:
        correct = ["a", "b"]


winning = True
score = 0

print(logo)
random_choices(random.choice(data), random.choice(data))

while winning:
    # To find follower count in previously established choices:
    compare_followers(choices[0]['follower_count'], choices[1]['follower_count'])

    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n"*50)
    print(logo)

    # To check if user has answered correctly:
    if user_answer in correct:
        score += 1
        print(f"You're right! Current score: {score}")
        random_choices(choices[1], random.choice(data))
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        winning = False


