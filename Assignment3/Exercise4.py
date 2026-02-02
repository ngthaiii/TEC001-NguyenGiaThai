import random
print("Welcome to the number guessing game!")
secret_number = random.randint(1,10)
while True:
    guess = int(input("Guess a number: "))
    if guess > secret_number:
        print("Too high.")
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Correct.")
        break
print("Congratulations on the victory!")