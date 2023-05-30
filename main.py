import requests
import datetime

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
TOKEN = "*************"
USERNAME = "balala"

# create user
USER_PARAMETERS = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMETERS)
# print(response.text)


# create a graph to track a certain habit
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "graph1"

GRAPH_PARAMETERS = {
    "id":GRAPH_ID,
    "name":"Run",
    "unit":"Km",
    "type":"float",
    "color":"shibafu",

}


# use header to authenticate
HEADERS = {
    "X-USER-TOKEN":TOKEN
}
# r = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_PARAMETERS, headers=HEADERS)



# add data
# today = datetime.datetime.now()
today = datetime.date(year=2023, month=5, day=29)
today_formatted = today.strftime("%Y%m%d")

PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
PIXEL_DATA = {
    "date": today_formatted,
    "quantity":"3",
}

# r = requests.post(url=PIXEL_ENDPOINT, json=PIXEL_DATA, headers=HEADERS)
# print(r.text)



# update data
UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today_formatted}"
UPDATE_DATA = {
    "quantity":"4.0"
}

# r = requests.put(url=UPDATE_ENDPOINT, json=UPDATE_DATA, headers=HEADERS)
# print(r.text)



# delete data
DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today_formatted}"
r = requests.delete(url=DELETE_ENDPOINT, headers=HEADERS)
print(r.text)
