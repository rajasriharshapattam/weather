url = "https://open-weather13.p.rapidapi.com/city"

querystring = {"city":"hyderabad","lang":"EN"}

headers = {
	"x-rapidapi-key": "cd1f759f71mshae99f9fa8ba0469p1c91b3jsn091dd289c435",
	"x-rapidapi-host": "open-weather13.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
