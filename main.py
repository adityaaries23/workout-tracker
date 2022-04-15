import requests
from datetime import datetime
import os

API_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
sheety_username = os.environ["sheety_username"]
sheety_password = os.environ["sheety_password"]

exercise = input("what exercise u do? ")
gender = "male"
weight = 80
height = 168
age = 28
end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_end_point = "https://api.sheety.co/f0cde626feb2874aa64dff9b6543069f/myWorkouts/workouts"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}
params = {
    "query": exercise,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age,
}

req = requests.post(url=end_point, headers=headers, json=params)
result = req.json()
print(result)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

header_sheety = {
    "Authorization": "Basic YWRpZGl0eWE1MjpkcWpud2RqMmoxMmU="
}

for i in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": i["name"].title(),
            "duration": i["duration_min"],
            "calories": i["nf_calories"]
        }
    }
    response = requests.post(url=sheet_end_point, json=sheet_inputs, headers=header_sheety)
    print(response.text)
