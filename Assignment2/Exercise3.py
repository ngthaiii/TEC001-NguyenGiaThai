def check_hemoglobin():
    sex = input("Enter your biological sex (male/female): ")
    if sex != "female" and sex != "male":
        print("Invalid sex.")
        return

    hemoglobin = int(input("Enter your hemoglobin value (g/l): "))
    if sex == "female":
        if hemoglobin < 117:
            print("Your hemoglobin is too low.")
        elif hemoglobin > 155:
            print("Your hemoglobin is too high.")
        else:
            print("Your hemoglobin is normal.")

    else:
        if hemoglobin < 134:
            print("Your hemoglobin is too low.")
        elif hemoglobin > 167:
            print("Your hemoglobin is too high.")
        else:
            print("Your hemoglobin is normal.")

check_hemoglobin()