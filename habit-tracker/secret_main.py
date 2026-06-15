import requests
from datetime import datetime
import os

PIXELA_USERNAME = os.environ.get("USERNAME")
PIXELA_TOKEN = os.environ.get("TOKEN")
PIXELA_GRAPH_ID = os.environ.get("GRAPH_ID")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"

graph_config = {
    "id": PIXELA_GRAPH_ID,
    "name": "Walking Graph",
    "unit": "Steps",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#------------------------------------ FOR ADDING NEW DATA --------------------------- #


pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"
today = datetime.now()
# today = datetime(year=2026, month=6, day=13)

pixel_creation_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many steps did you walk today? ")
}

response = requests.post(url=pixel_endpoint, json=pixel_creation_data, headers=headers)
print(response.text)


# ------------------------------------------------------------------------------------ #

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# new_pixel_data = {
#     "quantity": "44"
# }

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# delete_endpoint = update_endpoint
#
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

