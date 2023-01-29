import requests

API_KEY = "6a3419f671a92697704059c10fe370d0"


def get_data(place, number_of_days, data_type):
    request = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    print(request)
    data = requests.get(request)
    print(data)
    return data


get_data('Toronto', 1, "Temperature")
