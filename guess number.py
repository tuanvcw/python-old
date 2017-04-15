# guess my number game

import random
i = 1
x = random.randint(1,10)

print("Try to guess the number from 1 to 10.")
while True:
      print("Attem number " + str(i))
      guess = input("Try your best:")
      if int(guess) == x:
          print("correct !!!")
          break
      elif int(guess) > x:
          print("too high, try again")
          i = i + 1
      else:
          print("too low, try again")
          i = i + 1
      
