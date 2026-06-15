import requests
while True:
    url="https://api.openweathermap.org/data/2.5/weather"
    city=input("Enter the name of the city of which you want weather of: ")
    if city=="exit" or city=="quit":
        break
    try:
        params={
            "q":city,
            "appid":"dc61cab64ffdb8d03cde7279811ca7e4",
            "units": "metric"
        }
        response=requests.get(url,params=params)
        response.raise_for_status()
        print("Status code:",response.status_code)
        data=response.json()
        # print(f"\nJSON: {data}")
        print(f"\nCity: {data["name"]}")
        print(f"\nTemperature: {data["main"]["temp"]}°C")
        print(f"\nWeather description: {data["weather"][0]["description"]}")
        print(f"\nHumidity: {data["main"]["humidity"]}%")
    except Exception as e:
        print(e)
print("Program ended!")
print("out")