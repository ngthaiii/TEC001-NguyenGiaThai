import re
check = r"^[A-Z]{2,3}\d{3}$"
def check_course():
    while True:
        course = input("Enter the course code:")
        if course == "":
            print("Goodbye!")
            break
        if re.match(check, course):
            print("True")
        else:
            print("False")
check_course()