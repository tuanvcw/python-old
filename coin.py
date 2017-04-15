# flip coin
import random
i = 0
head = 0
tail = 0
while i < 100:
    x = random.randint(1,2)
    if x == 1:
        head+=1
        i+=1
    else:
        tail+=1
        i+=1

print("head: " + str(head))
print("tail: " + str(tail))
