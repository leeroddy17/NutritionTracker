import requests
import operator

def createUrl(queryterm):
    queryterm = queryterm.replace(" ", "%20")
    url = "https://nutritionix-api.p.rapidapi.com/v1_1/search/" + queryterm
    return url

def querry(querry):
    url = createUrl(querry)

    querystring = {"fields":"item_name,item_id,brand_name,nf_calories,nf_serving_weight_grams"}

    headers = {
        "X-RapidAPI-Host": "nutritionix-api.p.rapidapi.com",
        "X-RapidAPI-Key": "2f50ca2397mshff1a209d8be093ap1c0772jsn0f2d7d8caca4"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    dictionary = response.json()
    for i in dictionary["hits"]:
        print(i)
    return dictionary["hits"]

def rankBy(hits, sortingTerm):
    caloryRank = {}
    for i in hits:
        caloryRank[i['_id']] = i["fields"][sortingTerm]/i["fields"]["nf_serving_size_qty"]/i["fields"]["nf_serving_weight_grams"]

    sortedDict = dict(sorted(caloryRank.items(),key=operator.itemgetter(1),reverse=True))
    for i in sortedDict:
        for item in hits:
            if item['_id'] == i:
                print(item['fields']['item_name'],sortedDict[i])
    return sortedDict 



# get user input, dummy input rn since front end not created yet
queryterm = "cheddar cheese"

hits = querry(queryterm)

print(rankBy(hits, "nf_calories"))
