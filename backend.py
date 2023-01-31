import requests

API_KEY = "6a3419f671a92697704059c10fe370d0"


def get_data(place="Toronto", number_of_days=3, data_type="Temperature"):
    request = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    print(request)

    data = requests.get(request).json()

    data_dict = {}
    try:
        if data_type == "Temperature":
            for thing in data["list"][:number_of_days * 8]:
                data_dict[thing["dt_txt"]] = float(thing["main"]["temp"]) / 10
            return data_dict

        elif data_type == "Sky":
            for thing in data["list"][:number_of_days * 8]:
                data_dict[thing["dt_txt"]] = thing["weather"][0]["main"]
            return data_dict
    except KeyError:
        return None


if __name__ == "__main__":
    get_data('Tokyo', 3, "Sky")
