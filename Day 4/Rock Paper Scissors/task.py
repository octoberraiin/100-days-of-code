import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


rock_paper_scissors = [rock, paper, scissors]
ask = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
result = ""

if ask == 0:
    result = rock
    print(result)
elif ask == 1:
    result = paper
    print(result)
elif ask == 2:
    result = scissors
    print(result)
else:
    print("Invalid input")

random_rock_paper_scissors = random.choice(rock_paper_scissors)
print("Computer chose: \n", random_rock_paper_scissors)

if (ask == 0 and random_rock_paper_scissors == paper) or (ask == 1 and random_rock_paper_scissors == scissors) or (ask == 2 and random_rock_paper_scissors == rock):
    print("You lose!")
elif (ask == 1 and random_rock_paper_scissors == rock) or (ask == 2 and random_rock_paper_scissors == paper) or (ask == 0 and random_rock_paper_scissors == scissors):
    print("You win!")
elif result == random_rock_paper_scissors:
    print("It's a tie!")
else:
    print("Invalid input. YOU LOSE!")