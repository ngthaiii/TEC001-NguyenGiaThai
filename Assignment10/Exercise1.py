import requests
response = requests.get("https://api.chucknorris.io/jokes/random")
data= response.json()
joke_text = data["value"]
print(joke_text)