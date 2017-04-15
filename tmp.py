import random

sentence = input("enter the sentence to drop: ")
new_sentence = ""
vowel = "aeiou"

for letter in sentence:
    if letter.lower() not in vowel:
        new_sentence += letter
        print("new boy: ", new_sentence)

