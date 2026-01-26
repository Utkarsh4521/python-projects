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