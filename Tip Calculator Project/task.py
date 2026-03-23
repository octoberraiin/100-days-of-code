print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $\n "))
tip = int(input("What percentage tip would you like to give? 10 12 15\n "))
people = int(input("How many people to split the bill?\n "))

final = ((tip/100 * bill) + bill)/people
# This is basically: tip percentage of total bill + the fixed bill, all divided by number of people

formatted_final = f"{final:.2f}"
# To get that bill effect (rounded to 2 numbers)

print(f"Each person should pay: ${formatted_final}")
# f-string is taken as I want it quicker. The other method also works.
