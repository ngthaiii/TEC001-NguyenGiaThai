import random

print("Your 3-digits code:", end="")
for i in range(3):
    a = random.randint(0,9)
    print (a, end=" ")

print("\nYour 4-digits code:", end="")
for i in range(4):
    b = random.randint(1,6)
    print(b, end=" ")