def check_leap_year():
    year = int(input("Enter a year: "))
    if year % 400 == 0: #Divisible by 400
        print("The year is a leap year.")
    elif year % 4 == 0: #Divisible by 4 but not divisible by 100
        print("The year is a leap year.")
    elif year % 100 ==0: #Divisible by 100 but not divisible by 400
        print("The year is not a leap year.")
    else:
        print("The year is not a leap year.")

check_leap_year()