import json
import random
detailedData = []
print("Starting to read file")
with open("./80.json", "r") as content:
    detailedData = json.load(content)
print("Finished reading files")
mainData = []
counter = 0
for a in detailedData:
    seedFunding = a["points"]
    numberOfPeople = a["numberOfConnection"]
    a = a["user"]
    numberOfIndustries = 0
    for b in a["focusAreas"]:
        numberOfIndustries += len(b["sectors"])
    numberOfPortfolios = 0
    if(a["portfolios"]):
        numberOfPortfolios = len(a["portfolios"])
    govtFunded = 0
    if(a["govtFunded"]):
        govtFunded += 2
    numberOfPeople = max(len(a["contacts"]), numberOfPeople)
    a["seed_funding_score"] = random.randint(50, 100)
    a["physical_amenities"] = seedFunding
    a["talent_score"] = numberOfPeople*numberOfIndustries
    a["further_funding"] = govtFunded+numberOfPortfolios

    mainData.append(a)

with open('./scores/80_.json', 'w') as outfile:
    json.dump(mainData, outfile)
