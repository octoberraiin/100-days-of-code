sum = 0
for i in range(0, 101):
    sum += i

print(sum)

# The following was a fun test that I got right on the first try!
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

