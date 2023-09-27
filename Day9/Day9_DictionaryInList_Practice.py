travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def addNewCountry(countryVisited, timesVisited, citiesVisited):
    newCoutnry = {}
    newCoutnry["country"] = countryVisited
    newCoutnry["visits"] = timesVisited
    newCoutnry["cities"] = citiesVisited
    travel_log.append(newCoutnry) #리스트에 추가




#🚨 Do not change the code below
addNewCountry("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



