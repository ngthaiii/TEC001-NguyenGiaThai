import math
def unit_price(diameter_cm, price):
    diameter_m = (diameter_cm/100) #cm -> m
    area = math.pi * diameter_m
    return price/area

D1 = float(input("Enter the diameter of pizza 1 (cm): "))
P1 = float(input("Enter the price of pizza 1 (USD): "))

D2 = float(input("Enter the diameter of pizza 2 (cm): "))
P2 = float(input("Enter the price of pizza 2 (USD): "))

price1 = unit_price(D1,P1)
price2 = unit_price(D2,P2)

if price1 < price2:
    print("The pizza 1 is better value for money.")
elif price1 > price2:
    print("The pizza 2 is better value for money. ")
else:
    print(" Both pizzas provide the same value for money.")