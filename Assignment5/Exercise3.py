import re
find = r"\d+"
def sum_numbers():
    while True:
        text = input("Enter the paragraph:")
        if text == "":
            break
        numbers = re.findall(find, text)
        if numbers:
            total_sum = sum(int(n) for n in numbers)
            print(f"The sum:{total_sum}")
        else:
            print("No numbers found in the paragraph.")
sum_numbers()