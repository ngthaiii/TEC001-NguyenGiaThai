list_num = []
while True:
    num = input("Enter a number:")
    if num == "":
        break
    list_num.append(int(num))
list_num.sort(reverse=True)
final = list_num[:5]
print(f"The five largest numbers are: {final}")