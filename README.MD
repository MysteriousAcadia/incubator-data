# Steps Followed:

## Gathering Raw Data
The raw data was collected from mygovt.in website(lookup the proper website). Total data for 400 incubators was collected which were based in India and open.
The data was collected by capturing the GET request made by the website to fetch all incubator data. The data received was in the form of json.
<hr/>

## Filtering and clearing data
The original data was too big(see detailedData.json file). Unnecessary data fields were removed. THen the incubators that contained no data(website link or portfolio) were also removed. Finally we had around 80 incubators

<hr/>

## Filling the gaps
Finally, there were entries who did not have the linkedin url for their incubator, or the startups theiy funded. For those companies data was collected from google manually.