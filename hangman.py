# hangman game
import random

HANGMAN = (
"""
=====
""",
"""
====
""",
"""
===
""",
"""
==
""",
"""
=
"""
)

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("PYTHON", "MANA", "MONKEY")

# variables
word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

print("Welcome to hangman game")

while wrong <= MAX_WRONG and so_far !=word:
    print(HANGMAN[wrong])
    print("You already used these letters: ", used)
    print("The word is: ", so_far)
    print("The number of incorrect guess remain: ", 5-wrong)

    guess = input("Enter the letter: ")
    guess = guess.upper()

    while guess in used:
        print("You already guess this letter")
        guess = input("Enter the letter: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("Correct !", guess, "is in word")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("Not found !!!")
        wrong += 1

if wrong > MAX_WRONG:
    print("\nYou man is DEAD !!! LOSER !!!")
else:
    print("\nCongratulation, you WIN !!!")

print("The answer is: ", word)

input("Press Enter to exit")
