def remove_uneven(number):
    even_list = []
    for num in number:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
def original():
    original_list = []
    while True:
        origin = input("Enter an integer:")
        if origin == "":
            break
        original_list.append(int(origin))
    remove_list = remove_uneven(original_list)
    remove_list.sort()
    print(f"The original list is: {original_list}."
          f"\nThe list after remove odd numbers: {remove_list}.")
original()