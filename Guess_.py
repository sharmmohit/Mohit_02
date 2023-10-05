import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("Guess The Number b/w 1-10 = ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")