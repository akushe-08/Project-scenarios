import requests

url = "https://shazam.p.rapidapi.com/shazam-events/list"

querystring = {"artistId":"73406786","l":"en-US","from":"2022-12-31","limit":"50","offset":"0"}

headers = {
	"X-RapidAPI-Key": "063d989a58msh474c5b9f3032b41p19e7e0jsnc6a68e5bd6e0",
	"X-RapidAPI-Host": "shazam.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)