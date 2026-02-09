def calculate (number):
    return sum(number)
numbers_list = []
while True:
    num = input("Enter an integer: ")
    if num == "":
        break
    numbers_list.append(int(num))
total = sum(numbers_list)
print(f"The number list is: {numbers_list}.")
print(f"The sum is: {total}.")