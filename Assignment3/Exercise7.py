phrase = input("Enter a phrase: ")
def make_acronym():
    words = phrase.split()
    first_letters = []
    for word in words:
        first_letters.append(word[0].upper())
    acronym = "".join(first_letters)
    return acronym
print(f"The acronym is: {make_acronym()}")