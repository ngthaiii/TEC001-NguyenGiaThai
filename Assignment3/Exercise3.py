numbers = []
while True:
    user_input = input("Enter the number: ")
    if user_input == "":
        print("The program has stopped.")
        break
    num = float(user_input)
    numbers.append(num)
    if numbers:
        largest = max(numbers)
        smallest = min(numbers)
        print(f"Largest: {largest}")
        print(f"Smallest: {smallest}")
    else:
        print("You have not entered numbers yet.")