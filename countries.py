import requests
import json

#REST API link.
uri="https://restcountries.eu/rest/v2/all"

#Getting the api.
req=requests.get(uri)

country_full_detail=req.json()

#printing the countires names.

for i in country_full_detail:
 print(i[0])

#TODO: build a page that shows the coutires names and upon selection gives the basic details like the languages, population, area and other related stuff.


