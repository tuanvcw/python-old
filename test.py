import random
menu = []
for t in range(3):
    dish = input("")
    menu.append(dish)
for l in range(2):
    dish = input("")
    menu.append(dish)
print(menu[random.randrange(len(menu))])
