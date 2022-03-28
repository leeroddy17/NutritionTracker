import requests
import operator
import math

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

def rankBy(hits,cat,incr = True):
    catRank = {}
    scores = {}
    normalizedScores = 0
    normalizedCat = 0
    
    for i in hits:
        catRank[i['_id']] = [i['_score'],0]
        catRank[i['_id']][1] = i["fields"][cat]/i["fields"]["nf_serving_size_qty"]/i["fields"]["nf_serving_weight_grams"]
        
        normalizedScores += i['_score']**2        
        normalizedCat += (i["fields"][cat]/i["fields"]["nf_serving_size_qty"]/i["fields"]["nf_serving_weight_grams"])**2
        
    normalizedScores = math.sqrt(normalizedScores)
    normalizedCat = math.sqrt(normalizedCat)
    
    for i in catRank:
        catRank[i][0] /= normalizedScores
        catRank[i][1] /= normalizedCat
    if (incr):
        rankedDict = {i : (catRank[i][0]+catRank[i][1]) for i in catRank}
    else:
        rankedDict = {i : (catRank[i][0]-catRank[i][1]) for i in catRank}
    rankedDict = dict(sorted(rankedDict.items(),key=(operator.itemgetter(1)),reverse=True))
    for i in rankedDict:
        for item in hits:
            if item['_id'] == i:
                print(item['fields']['item_name'],catRank[i][0],catRank[i][1],rankedDict[i])
    return rankedDict



# this will be gotten by user input, dummy input rn since front end not created yet
queryterm = "cheddar cheese"
rankbyvalue = "nf_calories"

hits = querry(queryterm)
increasing = False

print(rankBy(hits, rankbyvalue, increasing))
