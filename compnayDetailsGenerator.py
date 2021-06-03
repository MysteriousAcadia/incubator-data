import requests
import json
MAIN_DATA_URL = "https://api.startupindia.gov.in/sih/api/common/user/profile/"
CONNECTIONS_ACCEPTED_URL = "https://api.startupindia.gov.in/sih/api/common/connection-accepted/stats/"
REVIEWS_URL = "https://api.startupindia.gov.in/sih/api/common/user/"
AVERAGE_REVIEW_URL = "https://api.startupindia.gov.in/sih/api/common/user/"
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
          "sort": {"orders": [{"field": "registeredOn", "direction": "DESC"}]},
          "dpiitRecogniseUser": False,
          "internationalUser": False}


def companyDetail(profileID):
    mainURL = MAIN_DATA_URL + profileID
    connectionAccepted = CONNECTIONS_ACCEPTED_URL + profileID
    reviews = REVIEWS_URL + profileID + "/reviews"
    reviewSummary = AVERAGE_REVIEW_URL + profileID + "/reviews/average"
    response = requests.get(mainURL, headers=headers)
    responseConnectionAccepted = requests.get(
        connectionAccepted, headers=headers)
    responseReviews = requests.get(reviews, headers=headers)
    responseReviewsSummary = requests.get(reviewSummary, headers=headers)
    mainData = json.loads(response.content)
    mainData["connectionAccepted"] = str(responseConnectionAccepted.content)
    mainData["responseReviews"] = json.loads(responseReviews.content)
    mainData["responseReviewsSummary"] = json.loads(
        responseReviewsSummary.content)
    return mainData


listofid = []
with open("listOfIds.txt", "r") as content:
    listofid = json.load(content)

mainData = []
counter = 0
for a in listofid:
    counter += 1
    if (counter % 10 == 0):
        print(counter)
    mainData.append(companyDetail(a))


with open('detailedData.json', 'w') as outfile:
    json.dump(mainData, outfile)
