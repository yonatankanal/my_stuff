list_o_guesses = []

import random
import sys

def main():
    make_number()
    print("Correct! Nice Job!")

def make_number():
    min = int(input("What should I think of a number between?\nMin: "))
    max = int(input("Max: "))
    try:
        number = random.randint(min,max)
    except ValueError:
        sys.exit("Follow the rules, darn you!")
    bad_guess = True
    while bad_guess:
        guess = input("Guess: ")
        if int(guess) > number:
            print("Too high.")
        elif int(guess) < number:
            print("Too low.")
        elif int(guess) == number:
            bad_guess = False
        insult(min,max,guess)
        if int(guess) < number:
            if int(guess) > min:
                min = int(guess) + 1
        elif int(guess) > number:
            if int(guess) < max:
                max = int(guess) - 1


def insult(min,max,guess):

   if guess in list_o_guesses:
        print(f"You guessed that already. You're dumber than a panda!")
   elif int(guess) < min:
        print(f"You are an idiot. It is impossible that {guess} is the number I am thinking of based on your previous guesses. {min} is the minimum number it can be.")
   elif int(guess) > max:
        print(f"You are an idiot. It is impossible that {guess} is the number I am thinking of based on your previous guesses. {max} is the maximum number it can be.")

   list_o_guesses.append(guess)


if __name__ == "__main__":
    main()