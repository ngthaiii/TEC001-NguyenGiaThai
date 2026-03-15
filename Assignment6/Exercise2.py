season = ("winter", "spring", "summer", "autumn")
month = int(input("Enter a month:"))
respective = (month % 12) // 3
print (f"The season is {season[respective]}.")