import requests;
import json;
import compnayDetailsGenerator;
MAIN_URL = "https://api.startupindia.gov.in/sih/api/noauth/search/profiles";
headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
"accept-encoding": "gzip, deflate, br",
"accept-language": "en,en-US;q=0.9,hi;q=0.8,kn;q=0.7",
"content-type": "application/json",
"origin": "https://www.startupindia.gov.in",
"referer": "https://www.startupindia.gov.in/",

"sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not\\A\"Brand";v="99"',
"sec-ch-ua-mobile": '?1',
"sec-fetch-dest": 'empty',
"sec-fetch-mode": 'cors',
"sec-fetch-site": 'same-site',
"user-agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36'
}
params = {"query": "",
"focusSector": False,
"industries": [],
"sectors": [],
"states": [],
"cities": [],
"stages": [],
"badges": [],
"roles": ["Incubator"],
"page": 1,
"sort": {"orders": [{"field":"registeredOn", "direction":"DESC"}]},
"dpiitRecogniseUser": False,
"internationalUser":False};
allContent = [];
allIds = [];
for i in range(1,79):
    params["page"] = i;
    response = requests.post(MAIN_URL, headers=headers, json=params);
    y = json.loads(response.content);
    y = y['content'];
    for a in y:
        allIds.append(a["id"]);
    allContent+=y;
with open('data.txt', 'w') as outfile:
    json.dump(allContent, outfile);
    
with open('listOfIds.txt', 'w') as outfile:
    json.dump(allIds,outfile);

detailedContent = [];
counter = 0;
for a in allIds:
    counter += 1;
    if (counter % 10 == 0){
        print(counter);
    }
    detailedContent.append(compnayDetailsGenerator.companyDetail(a));

with open('detailedData.txt', 'w') as outfile:
    json.dump(detailedContent,outfile);