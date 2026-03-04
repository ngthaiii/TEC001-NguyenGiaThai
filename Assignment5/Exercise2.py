import re
regex = r"^#[0-9A-Fa-f]{6}$"
def check_colour():
    while True:
        colour = input("Enter a hex color code:")
        if colour == "":
            print("Goodbye!")
            break
        if re.match(regex, colour):
            print("Colour is a valid hex.")
        else:
            print("Colour is not a valid hex.")
check_colour()