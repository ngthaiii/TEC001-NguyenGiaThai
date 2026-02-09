numbers = []
while True:
    num = input("Enter a number: ")
    if num == "":
        break
    numbers.append(int(num))
numbers.sort(reverse=True)
final = numbers[:5]
print(f"The five largest numbers are: {final}")