import json
import csv
import requests
import time

url = 'https://api.chambers.com/api/organisations/250204/ranked-lawyers?publicationTypeId=2'
url2 = 'https://api.chambers.com/api/organisations/111/ranked-lawyers?publicationTypeId=7'

data = requests.get(url2).text
data = json.loads(data)


outputFile = open("data.csv", "w")
outputWriter = csv.writer(outputFile)

publisher = 'Chambers and Partners'

start = time.time()

for i in data:
    row_array = []
    row_array.append(data["description"])
    for group in data["groups"]:
        row_array.append(group["type"])
        for practice in group["practiceAreas"]:
            row_array.append(practice["id"])
            row_array.append(practice["description"])
            for location in practice["individualsInLocations"]:
                row_array.append(location["id"])
                row_array.append(location["description"])
                for person in location["rankedEntities"]:
                    row_array.append(person["personOrganisationId"])
                    row_array.append(person["displayName"])
                    for ranking in person["rankings"]:
                        row_array.append(ranking["rankingDescription"])
        

        
        
    outputWriter.writerow(row_array)
    
    

outputFile.close()    
        
end = time.time()
print(end - start)

