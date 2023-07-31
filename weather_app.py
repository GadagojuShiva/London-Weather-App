import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"

def get_weather_data(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.json()['message']}")
        return None

def get_weather_by_date(data, date):
    for item in data["list"]:
        if item["dt_txt"].startswith(date):
            return item["main"]["temp"]
    return None

def get_wind_speed_by_date(data, date):
    for item in data["list"]:
        if item["dt_txt"].startswith(date):
            return item["wind"]["speed"]
    return None

def get_pressure_by_date(data, date):
    for item in data["list"]:
        if item["dt_txt"].startswith(date):
            return item["main"]["pressure"]
    return None

def main():
    city = "London"
    data = get_weather_data(city)
    if not data:
        return

    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "0":
            break
        elif choice == "1":
            date = input("Enter the date (yyyy-mm-dd): ")
            temp = get_weather_by_date(data, date)
            if temp is not None:
                print(f"Temperature on {date}: {temp} K")
            else:
                print("Data not available for the given date.")
        elif choice == "2":
            date = input("Enter the date (yyyy-mm-dd): ")
            wind_speed = get_wind_speed_by_date(data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not available for the given date.")
        elif choice == "3":
            date = input("Enter the date (yyyy-mm-dd): ")
            pressure = get_pressure_by_date(data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not available for the given date.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
