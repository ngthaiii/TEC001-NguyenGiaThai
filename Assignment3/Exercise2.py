while True:
    inch = float(input("Enter the inch: "))
    if inch >= 0: #inch = 2.54cm
        cm = inch * 2.54
        print(f"{inch} inch = {cm} cm")
    else:
        print("The program has stopped.")
        break