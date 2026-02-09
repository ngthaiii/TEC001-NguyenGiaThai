def remove_odd(number):
    even_list = []
    for i in number:
        if i % 2 == 0:
            even_list.append(i)
    return even_list
def origin():
    original_list = []
    while True:
        num = input("Enter an integer: ")
        if num == "":
            break
        original_list.append(int(num))
    short_list = remove_odd(original_list)
    short_list.sort()
    print(f"The original list is: {original_list}.")
    print(f"The short list is: {short_list}.")
origin()