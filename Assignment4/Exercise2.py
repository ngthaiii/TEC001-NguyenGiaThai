num = int(input("Enter an integer number: "))
prime = False
if num > 1:
    prime = True
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        prime = False
        break
if prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")