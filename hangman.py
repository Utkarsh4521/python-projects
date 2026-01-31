import random
import time

print("\nWelcome to Hangman game \n")
name = input("Enter your name: ")
print("The game is about to start!\n Get ready, " + name + "!\n")
time.sleep(3)  # i m doing this to delay the game for 3 seconds.
def main():
    words_to_guess = ["january","border","image","film","promise","kids","lungs","valo","doll","rhyme","damage","plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    return word, display, count, already_guessed, length
def rounds():
    play = input("Do You want to play again? y = yes, n = no \n").lower()

    while play not in ["y", "n"]:
        play = input("Please enter correctly. y = yes, n = no \n").lower()
    return play == "y"
def hangman(word, display, count, already_guessed, length):
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid Input, Try a letter\n")
        return hangman(word, display, count, already_guessed, length)
    elif guess in word:
        already_guessed.append(guess)
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print(r"""  _____
                   |     | 
                   |     |
                   |     | 
                   |     O 
                   |    /|\ 
                   |    / \ 
                  _|__""")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")

    elif count != limit:
        hangman(word, display, count, already_guessed, length)


while True:
    word, display, count, already_guessed, length = main()
    hangman(word, display, count, already_guessed, length)

    if not rounds():
        print("Thanks For Playing!")
        break


