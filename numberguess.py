#this is a rock paper scissor game that a user can play with the computer system .
# on running the program a new window pops up that interacts with the user via buttons .
import random
n = random.randrange(1,100)
guess = int(input("Enter any number: "))
while n!= guess:
    # if guess is smaller than n
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    # if guess is greater than n
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
        break

print("you guessed it right!!")
