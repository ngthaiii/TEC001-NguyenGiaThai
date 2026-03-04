import re
hide = r"\+84\d+|\d{10}"
def hide_number():
    text = input("Enter a document:")
    if text == "":
        print("The document is empty.")
        return
    hide_numbers = re.sub(hide,"[REDACTED]",text)
    print(hide_numbers)
hide_number()