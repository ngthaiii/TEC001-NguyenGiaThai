text = input("Enter your string: ")
def extract_middle():
    length = len(text)
    middle = length // 2
    if length % 2 == 0:
        return text[middle - 1 : middle + 1]
    else:
        return text[middle]
print(f"Middle character: {extract_middle()}")
