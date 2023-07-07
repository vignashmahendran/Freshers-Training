import requests
import json
import pandas as pd
hero_id=pd.read_html("https://www.superheroapi.com/ids.html")[0]
print(" "*20 +"----Get all SuperHeroes and Villians data from all universes----")
print(hero_id.iloc[:49,1:])
search_id=str(int(input("Enter Id of the character:"))+1)
response=requests.get(f"https://akabab.github.io/superhero-api/api/id/{search_id}.json")
details=response.json()
response=response.json()
with open('text.json','w') as e:
    json.dump(response,e,indent=4)
r=pd.read_json('text.json')
r.to_csv('file.csv')
print(" "*20 +"---------------"+ details["name"] +"---------------")

print(" "*25 +"---------"+ "powerstats"+"---------")
for value in details["powerstats"]:
    print(" "*30 +str(value) +" : "+ str(details["powerstats"][value]) )    

print(" "*25 +"---------"+ "appearance"+"---------")
for value in details["appearance"]:
    print(" "*30 +str(value) +" : "+ str(details["appearance"][value]) )    
    
print(" "*25 +"---------"+ "biography"+"---------")
for value in details["biography"]:
    print(" "*30 +str(value) +" : "+ str(details["biography"][value]) )    
print(" "*25 +"---------"+ "work"+"---------")
for value in details["work"]:
    print(" "*12 +str(value) +" : "+ str(details["work"][value]) )    
