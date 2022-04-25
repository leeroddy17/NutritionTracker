import requests
import operator
import math

def createUrl(queryterm):
    queryterm = queryterm.replace(" ", "%20")
    url = "https://nutritionix-api.p.rapidapi.com/v1_1/search/" + queryterm
    return url

def querry(querry,fields=['item_name','brand_name','nf_calories','nf_serving_weight_grams','nf_total_fat','nf_total_carbohydrate','nf_dietary_fiber'
                        ,'nf_sodium','nf_cholesterol','nf_sugars','nf_protein','nf_potassium','nf_vitamin_d_mcg','nf_added_sugars','nf_ingredient_statement','item_description']):
    url = createUrl(querry)
    fieldString = ''
    for field in fields:
        fieldString += field + ',' 
    querystring = {"fields":fieldString[:-1]}

    headers = {
        "X-RapidAPI-Host": "nutritionix-api.p.rapidapi.com",
        "X-RapidAPI-Key": "2f50ca2397mshff1a209d8be093ap1c0772jsn0f2d7d8caca4"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    dictionary = response.json()
    # for i in dictionary["hits"]:
    #     print(i)
    return dictionary["hits"]

def querryNameOnly(querry):
    url = createUrl(querry)

    querystring = {"fields":"item_name,brand_name,item_id"}

    headers = {
        "X-RapidAPI-Host": "nutritionix-api.p.rapidapi.com",
        "X-RapidAPI-Key": "2f50ca2397mshff1a209d8be093ap1c0772jsn0f2d7d8caca4"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    dictionary = response.json()
    # for i in dictionary["hits"]:
    #     print(i)
    return dictionary["hits"]
def rankBy(hits,cat,incr = True):
    catRank = {}
    scores = {}
    orderedHits = {}
    normalizedScores = 0
    normalizedCat = 0
    
    for index, i in enumerate(hits):
        if(type(i[cat]) is not float and type(i[cat]) is not int):
            i[cat] = 0

        catRank[i['tags']['tag_id']] = [10-index,0]
        catRank[i['tags']['tag_id']][1] = i[cat]/float(i["serving_qty"])/float(i["serving_weight_grams"])
        
        normalizedScores += (10-index)**2        
        normalizedCat += (i[cat]/float(i["serving_qty"])/float(i["serving_weight_grams"])**2)
        
    normalizedScores = math.sqrt(normalizedScores)
    normalizedCat = math.sqrt(normalizedCat)

    if(normalizedScores == 0):
        normalizedScores = 1
    if(normalizedCat == 0):
        normalizedCat = 1
    
    for i in catRank:
        catRank[i][0] /= normalizedScores
        catRank[i][1] /= normalizedCat
    if (incr):
        rankedDict = {i : (catRank[i][0]+catRank[i][1]) for i in catRank}
    else:
        rankedDict = {i : (catRank[i][0]-catRank[i][1]) for i in catRank}
    rankedDict = list(dict(sorted(rankedDict.items(),key=(operator.itemgetter(1)),reverse=True)).keys())
    newHits = []
    for i in rankedDict:
        for j in hits:
            if (i==j['tags']['tag_id']):
                print(j['food_name'])
                newHits.append(j)
    return newHits



# this will be gotten by user input, dummy input rn since front end not created yet
"""
queryterm = "cheddar cheese"
rankbyvalue = "nf_calories"

hits = querry(queryterm)
increasing = False
for i in hits:
    print(i['fields']['item_name'])
newhits = rankBy(hits, rankbyvalue, increasing)
for i in newhits:
    print(i['fields']['item_name'])
"""

def findSuperlatives(list,field):
    if (len(list) > 1):
        maxIndex = 0
        maxVal = list[0]['fields'][field]
        minIndex = 0
        minVal = list[0]['fields'][field]
        for index, element in enumerate(list):
            if (element['fields'][field] > maxVal):
                maxVal = element['fields'][field]
                maxIndex = index
            elif (element['fields'][field] < minVal):
                minVal = element['fields'][field]
                minIndex = index
        print(maxIndex)
        print(maxVal)
        return minIndex,maxIndex
    return None, None
