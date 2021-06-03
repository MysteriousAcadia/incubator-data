import json
detailedData = []
print("Starting to read file")
with open("./detailedData.json", "r") as content:
    detailedData = json.load(content)
print("Finished reading files")
mainData = []
counter = 0
for a in detailedData:
    counter += 1
    if (counter % 10 == 0):
        print(counter)
    if(a["user"]["portfolios"]):
        mainData.append(a)

with open('iteration1.json', 'w') as outfile:
    json.dump(mainData, outfile)
