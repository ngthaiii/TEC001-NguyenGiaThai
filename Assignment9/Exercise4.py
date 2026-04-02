file = open("caesar.txt", "r")
tele = 3
direction = input("Choose your direction: ")
result = ""
if direction != "right" and direction != "left":
    print("Only choose either right or left.")
    exit()
for line in file:
    line = line.rstrip()
    for words in line:
        if words.isupper():
            if direction == "right":
                y = (ord(words) + tele - 65) % 26 + 65
            else:  # left
                y = (ord(words) - tele - 65) % 26 + 65
            result = result + chr(y)

        elif words.islower():
            if direction == "right":
                y = (ord(words) + tele - 97) % 26 + 97
            else:
                y = (ord(words) - tele - 97) % 26 + 97
            result = result + chr(y)

        else:
            result = result + words

file.close()

final = open("ciphertext.txt", "w")
final.write(result)
final.close()