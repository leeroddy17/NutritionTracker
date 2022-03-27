import requests

def rankByCalories():
	pass




url = "https://nutritionix-api.p.rapidapi.com/v1_1/search/cheddar%20cheese"

querystring = {"fields":"item_name,item_id,brand_name,nf_calories,nf_total_fat"}

headers = {
	"X-RapidAPI-Host": "nutritionix-api.p.rapidapi.com",
	"X-RapidAPI-Key": "274e0fe4e2msh35a56d59a1bc9b5p1b76c1jsn87091e6b16fa"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())
print(type(response.json()))