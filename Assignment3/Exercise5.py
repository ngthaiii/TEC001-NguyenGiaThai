correct_username = "python"
correct_password = "rules"
for i in range (5):
    username = input("Username: ")
    password = input("Password: ")
    if username == correct_username and password == correct_password :
        print("Welcome!!!")
        break
    else:
        remaining = 4 - i
    if remaining > 0:
        print(f"Incorrect. You have only {remaining} attempts left.")
    else:
        print("Access denied.")