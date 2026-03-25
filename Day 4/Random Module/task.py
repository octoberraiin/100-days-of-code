import random
import mymodule

# random_integer = random.randint(1, 10)
# print(random_integer)
# print(mymodule.my_favorite_number)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# print(random.choice(["heads", "tails"]))     # This is one way to do it (figured it out on my own)

random_heads_or_tails = random.randint(0, 1)     # This is a more basic format.
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")