import requests

url = "https://open-weather13.p.rapidapi.com/city"

querystring = {"city":"new york","lang":"EN"}

headers = {
	"x-rapidapi-key": "Sign Up for Key",
	"x-rapidapi-host": "open-weather13.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
