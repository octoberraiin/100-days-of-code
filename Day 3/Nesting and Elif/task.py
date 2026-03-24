print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input("What is your age? "))
    if age <= 12:
        print(str(age) + "!? " + "Some height you got bro")
    elif age <= 18:
        print("Go home. You " + str(age) + "-year-olds mess everything up.")
    else:
        if height <= 170:
            print("You're pretty short for " + str(age) + ".")
        else:
            print("You're pretty tall for " + str(age) + ". RESPECT!")
        print("Aren't a little too old for this though? Okay whatever... Don't die in the rollercoaster!")
else:
    print("Sorry you have to grow taller before you can ride.")
