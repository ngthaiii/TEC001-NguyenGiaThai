file = open("score.txt","r")
total = 0
students = 0
for line in file:
    line_clean = line.rstrip()
    if line != "":
        separation = line_clean.split(",")
        if len(separation) == 2:
            score = int(separation[1])
            total = total + score
            students = students + 1
if students > 0:
    average_score = total / students
    print(f"Average score: {average_score}")
else:
    print("No students found.")
file.close()