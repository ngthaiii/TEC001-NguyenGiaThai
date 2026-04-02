essay = open("mbox.txt", "r")
count = 0
for line in essay:
    line = line.rstrip()
    if line != "":
        count = count + 1
print("Line Count: ", count)
essay.close()