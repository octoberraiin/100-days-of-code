import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_friends = random.choice(friends)
print(random_friends)

# OR

random_numbers_for_bill = random.randint(0, 5)
if random_numbers_for_bill == 0:
    print("Alice")
elif random_numbers_for_bill == 1:
    print("Bob")
elif random_numbers_for_bill == 2:
    print("Charlie")
elif random_numbers_for_bill == 3:
    print("David")
else:
    print("Emanuel")

# OR

random_index = random.randint(0, 4)
print(friends[random_index])