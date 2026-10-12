#if you wanna see whats going on here just check ( README.txt ).


#importing requests package cuz we need it (wanna know why? check "README.txt" )
import requests

print('Welcome to Smart Weather Checker!'.title())

#defining get_coordinates
def get_coordinates(city):
    url = ('https://geocoding-api.open-meteo.com/v1/search')

    params = {
        'name': city,
        'language': 'en',
        'format': 'json',
        'count': 1
    }

    #to send request to our API to get needed informations
    response = requests.get(url, params=params, timeout=10)
    #checks the HTTP to see if conection is alright
    response.raise_for_status()

    data = response.json()
    results = data.get('results', [])

    if not results:
        print('Smt Went Wrong Finding The City!:(')
        return None

    location = results[0]

    latitude = location['latitude']
    longitude = location['longitude']

    #saves the informations we need(we gonna use it later)
    return latitude, longitude

#defining weather-checker
#this is where everything happens
def weather(city):

    #imports information that we got from get_coordination(saved with return cmd in line 38)
    coordinates = get_coordinates(city)
    if coordinates is None:
        print('Smt Went Wrong!:(')
        return None

    latitude, longitude = coordinates

    url = ('https://api.open-meteo.com/v1/forecast')

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code,is_day",
        "daily": (
            "temperature_2m_max,"
            "temperature_2m_min,"
            "daylight_duration,"
            "sunshine_duration,"
            "uv_index_max,"
            "wind_direction_10m_dominant"
        ),
        "forecast_days": 2,
        "timezone": "auto"
     }

    #sends request to our API
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    #enters to "current" dictionary to see its lists
    current = data.get("current", {})

    time = current.get("time")
    temperature = current.get("temperature_2m")
    humidity = current.get("relative_humidity_2m")
    wind_speed = current.get("wind_speed_10m")
    weather_code = current.get("weather_code")
    is_day = current.get("is_day")

    #enters to "daily" dictionary to see its lists
    daily = data.get("daily", {})

    min_temps = daily.get("temperature_2m_min", [])
    max_temps = daily.get("temperature_2m_max", [])

    if len(min_temps) < 2 or len(max_temps) < 2:
        print("Smt Went Wrong Finding Tomorrow's Temperature!:(")
        return None

    min_tomorrow = min_temps[1]
    max_tomorrow = max_temps[1]


    daylight_d = daily.get("daylight_duration", [])
    if len(daylight_d) < 2:
        print("Smt Went Wrong Finding Tomorrow's Daylight Duration!:(")
        return None

    daylight_duration = daylight_d[1]


    sun_d = daily.get("sunshine_duration", [])
    if len(sun_d) < 2:
        print("Smt Went Wrong Finding Tomorrow's Sunshine Duration!:(")
        return None

    sunshine_duration = sun_d[1]


    uv_i_m = daily.get("uv_index_max", [])
    if len(uv_i_m) < 2:
        print("Smt Went Wrong Finding Tomorrow's Maximum UV Index!:(")
        return None

    uv_index_max = uv_i_m[1]

    
    wind_direction = daily.get("wind_direction_10m_dominant")
    if wind_direction is None or len(wind_direction) < 2:
        print("Smt Went Wrong Finding Tomorrow's Wind Dominant Direction!:(")
        return None

    wind_direction_10m_dominant = wind_direction[1]


    #saves information for later...
    return (
        time,
        temperature,
        min_tomorrow,
        max_tomorrow,
        weather_code,
        humidity,
        wind_speed,
        wind_direction_10m_dominant,
        is_day,
        daylight_duration,
        sunshine_duration,
        uv_index_max
    )

#defining get_weather_description
def get_weather_description(code):
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Thunderstorm with heavy hail"
    }

    #saves information for later...
    return descriptions.get(code, "Unknown weather condition")


#asks the user what citys weather he wanna know
loca = input('Wich city is in your mind? (Please write it in English): ')


try:
    #sends city name to weather() to find coordinates
    #so we can find weather informations to give it to user
    results = weather(city=loca)
except requests.exceptions.Timeout as error:
    print(f"Request timed out: {error}")
    results = None
except requests.exceptions.ConnectionError as error:
    print(f"Connection error: {error}")
    results = None
except requests.exceptions.HTTPError as error:
    print(f"HTTP error occurred: {error}")
    results = None
except requests.exceptions.RequestException as error:
    print(f"An unexpected request error occurred: {error}")
    results = None

#its literally pure english
#you can understand by reading it :) 
if results is not None:
    (
        time,
        temperature,
        min_tomorrow,
        max_tomorrow,
        weather_code,
        humidity,
        wind_speed,
        wind_direction_10m_dominant,
        is_day,
        daylight_duration,
        sunshine_duration,
        uv_index_max
    ) = results

    daylight_duration = daylight_duration / 3600  # Convert seconds to hours
    sunshine_duration = sunshine_duration / 3600  # Convert seconds to hours

    print(f"Time: {time}")
    print(f"Temperature: {temperature}°C")
    print(f"Tomorrow's Minimum Temperature: {min_tomorrow}°C")
    print(f"Tomorrow's Maximum Temperature: {max_tomorrow}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} km/h")
    print(f'Wind Dominant Direction: {wind_direction_10m_dominant} degrees')
    print(f"Weather Description: {get_weather_description(weather_code)}")
    print(f"Is it Daytime? {'Yes' if is_day == 1 else 'No'}")
    print(f'Daylight Duration: {daylight_duration:.1f} hours')
    print(f'Sunshine Duration: {sunshine_duration:.1f} hours')
    print(f'Maximum UV Index is: {uv_index_max}')