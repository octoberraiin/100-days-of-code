from flask import Flask
from random import randint

app = Flask(__name__)

answer = str(randint(0, 9))
print(f"The answer is: {answer}")

@app.route('/')
def hello():
    return '<h1>Guess a number between 0 and 9</h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<user_guess>')
def guess_number(user_guess):
    if user_guess == answer:
        return '<h1 style="color: green">You found me!</h1>' \
                '<img src="https://media.giphy.com/media/jmrHF3wnU2Q38iwArI/giphy.gif">'
    elif user_guess < answer:
        return '<h1 style="color: red">Too low!</h1>' \
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif user_guess > answer:
        return '<h1 style="color: purple">Too high!</h1>' \
               '<img src="https://media.giphy.com/media/yXBqba0Zx8S4/giphy.gif">'
    return None


if __name__ == '__main__':
    app.run(debug=True, port=5002)