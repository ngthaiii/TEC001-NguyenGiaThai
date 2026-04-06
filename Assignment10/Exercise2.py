import requests
city_name = input("Enter the city name: ")
key = "d3a723f29588bb1fbf2f84fe585da1be"
data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}")
if data.status_code == 200:
    response = data.json()
    des = response["weather"][0]["description"]
    kelvin = response["main"]["temp"]
    celsius = kelvin - 273.15
    print(f"Weather at: {city_name}."
          f"\nDescription: {des}."
          f"\nTemperature: {celsius:.1f}°C.")
else:
    print(f"Weather not available for {city_name}.")