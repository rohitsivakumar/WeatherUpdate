# !/usr/bin/env python
"""
    Description: This program demonstrates the use of RESTAPI from https://openweathermap.org. to fetch the
    current weather details based on the city name.
    Author: Rohit Sivakumar
    Date: 10-AUG-2021
"""
import os
import requests
import time
import datetime

os.system("clear")
print(" * - * - * -  * - *")
print("Get Weather for your City using https://openweathermap.org")
api_key = input("Enter your openweathermap API KEY: ")
city = input("Enter name of city: ")
print(f'Fetching weather for "{city}"....')

api_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"


while True:
    resp = requests.get(api_url)
    if resp.status_code == 200:
        # print("Server returned: OK:", response.status_code)
        # print("Server headers:", response.headers['Content-Type'])
        result = resp.json()
        print("**************************************")
        print("City: {0}, Country: {1}".format(city, result['sys']['country']))
        print("Weather updated at: ", datetime.datetime.fromtimestamp(result['dt']).strftime('%d-%m-%Y, %H:%M:%S'))
        print("Longitude: {0}, Latitude: {1}".format(result['coord']['lon'], result['coord']['lat']))
        print("Sunrise:", datetime.datetime.fromtimestamp(result['sys']['sunrise']).strftime("%H:%M:%S"))
        print("Sunset:", datetime.datetime.fromtimestamp(result['sys']['sunset']).strftime("%H:%M:%S"))

        print("----------------------")
        print("WEATHER now: {0} - {1}".format(result['weather'][0]['main'], result['weather'][0]['description']))
        print("Temperature: ", round(result['main']['temp'], 2), u"\N{DEGREE SIGN}C")
        print("Feels like: {0} C, Min: {1} C, Max: {2} C".format(round(result['main']['feels_like'], 2),
                                                                 round(result['main']['temp_min'], 2),
                                                                 round(result['main']['temp_max'], 2)))
        print("Pressure: {0} hpa, Humidity: {1}%, Visibility: {2} Km".format(result['main']['pressure'],
                                                                             result['main']['humidity'],
                                                                             (result['visibility']) / 1000))
        wind_speed_in_degrees = result['wind']['deg']
        # Converting wind speed in degrees to Directional Compass quadrants
        wind_speed = wind_speed_in_degrees % 360
        wind_speed_sector = round(wind_speed / 22.5, 0) + 1
        if wind_speed_sector == 1:
            direction = "N"
        elif wind_speed_sector == 2:
            direction = "NNE"  # North-North East
        elif wind_speed_sector == 3:
            direction = "NE"  # North East
        elif wind_speed_sector == 4:
            direction = "ENE"  # East-North East
        elif wind_speed_sector == 5:
            direction = "E"
        elif wind_speed_sector == 6:
            direction = "ESE"
        elif wind_speed_sector == 7:
            direction = "SE"
        elif wind_speed_sector == 8:
            direction = "SSE"
        elif wind_speed_sector == 9:
            direction = "S"
        elif wind_speed_sector == 10:
            direction = "SSW"
        elif wind_speed_sector == 11:
            direction = "SW"
        elif wind_speed_sector == 12:
            direction = "WSW"
        elif wind_speed_sector == 13:
            direction = "W"
        elif wind_speed_sector == 14:
            direction = "WNW"
        elif wind_speed_sector == 15:
            direction = "NW"
        elif wind_speed_sector == 16:
            direction = "NNW"
        elif wind_speed_sector == 17:
            direction = "N"
        else:
            direction = " -- "
        print("Wind: {0} m/s, {1}".format(result['wind']['speed'], direction))

        print("\n###### AIR QUALITY DATA #########\n")
        air_api_url = "https://api.openweathermap.org/data/2.5/air_pollution/forecast?lat=" + str(
            result['coord']['lat']) + "&lon=" + str(result['coord']['lon']) + "&appid=" + api_key
        air_resp = requests.get(air_api_url)
        air_result = air_resp.json()
        quality = air_result['list'][0]['main']['aqi']
        if quality == 1:
            air = "Good"
        elif quality == 2:
            air = "Fair"
        elif quality == 3:
            air = "Moderate"
        elif quality == 4:
            air = "Poor"
        elif quality == 5:
            air = "Very Poor"
        print(f'Air quality Index:{quality}, meaning - {air}')
        print("Components")
        for component_name in air_result['list'][0]['components']:
            print("\t", component_name,":",air_result['list'][0]['components'][component_name])

        time.sleep(60)
        os.system("clear")
        print('updating . . . . ', end='\r')
    elif resp.status_code == 429:
        print("You made more than 60 API calls per minute (surpassing the limit of your subscription")
        break
    else:
        print(resp.status_code)
        break
