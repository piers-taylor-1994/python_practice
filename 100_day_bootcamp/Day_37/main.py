# import requests
# from datetime import *
# import time

# USERNAME = "pierstaylor23"
# TOKEN = "asdasd7sad7a7dsa7"
# GRAPH_ID = "graph1"

# PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# # response = requests.post(PIXELA_ENDPOINT, json={
# #     "token": "asdasd7sad7a7dsa7",
# #     "username": "pierstaylor23",
# #     "agreeTermsOfService": "yes",
# #     "notMinor": "yes"
# # })
# # print(response.text)

# graphic_params = {
#     "id": GRAPH_ID,
#     "name": "Coding graph",
#     "unit": "Mins",
#     "type": "int",
#     "color": "ajisai"
# }

# headers = {
#     "X-USER-TOKEN": TOKEN
# }

# # response = requests.post(f"{PIXELA_ENDPOINT}/{USERNAME}/graphs", json=graphic_params, headers=headers)
# # print(response.text)

# date_today = datetime.now()
# formatted_date = str(date_today.date()).replace("-", "")
# formatted_date_2 = date_today.strftime("%Y%m%d")

# minutes_coding = input("Enter how many minutes I practiced coding today: ")

# pixel_params = {
#     "date": f"{formatted_date}",
#     "quantity": minutes_coding,   
# }

# def call_api(attempt: int):
#     if attempt < 3:
#         try:
#             # Add pixel
#             response = requests.post(f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}", headers=headers, json=pixel_params)

#             #Update pixel
#             # response = requests.put(f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date_2}", headers=headers, json=pixel_params)

#             #Delete pixel
#             # response = requests.delete(f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date_2}", headers=headers)

#             response.raise_for_status()
#             print(response.text)
#         except:
#             print(f"Attempt {attempt + 1} faild. Trying again")
#             attempt += 1

#             time.sleep(1)
#             call_api(attempt)
# call_api(0)

word = "Hello"
print(word[::-1])