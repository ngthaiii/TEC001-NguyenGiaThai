essay = open("mbox.txt", "r")
keyword_list = []
current_line = 1
for line in essay:
    if "from" in line.lower():
        keyword_list.append(current_line)
        current_line += 1
print("Lines containing keywords: ", keyword_list)
essay.close()