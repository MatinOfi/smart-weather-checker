# 🌦️ Smart Weather Checker

A simple Python project that fetches real-time weather information and tomorrow's forecast for a city of your choice using the [Open-Meteo API](https://open-meteo.com/).

This project was built to practice Python fundamentals, working with APIs, handling HTTP requests, and processing JSON data.

## ✨ Features

- 🌍 **City Search:** Find a city's geographical coordinates using its name.
- 🌡️ **Current Temperature:** Display the current temperature in Celsius.
- 💧 **Humidity:** Show the current relative humidity.
- 💨 **Wind Information:** Display the current wind speed and tomorrow's dominant wind direction.
- 🌧️ **Weather Description:** Convert weather codes into readable descriptions.
- 📅 **Tomorrow's Forecast:** Display tomorrow's minimum and maximum temperatures.
- ☀️ **Daylight & Sunshine:** Show tomorrow's daylight and sunshine duration in hours.
- 🕶️ **UV Index:** Display tomorrow's maximum UV index.
- 🌞 **Day/Night Detection:** Check whether it is currently daytime or nighttime.
- 🛡️ **Error Handling:** Handle common request errors, including timeouts, connection errors, and HTTP errors.

## 🛠️ Technologies Used

- **Python**
- **Requests** for sending HTTP requests
- **Open-Meteo Geocoding API** for finding city coordinates
- **Open-Meteo Forecast API** for weather data

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MatinOfi/smart-weather-checker.git
```

### 2. Navigate to the Project Directory

```bash
cd smart-weather-checker
```

### 3. Install the Required Package

Make sure Python is installed, then run:

```bash
python -m pip install requests
```

### 4. Run the Program

```bash
python smart-weather-checker.py
```

Enter the name of a city in English when prompted, and the program will retrieve the available weather information.

## 📋 Example Output

The following is an illustrative example of what the program's output may look like. Actual values depend on the selected city and the weather API response.

```text
Welcome to Smart Weather Checker!

Wich city is in your mind? (Please write it in English): London

Time: 2026-10-13T14:00
Temperature: 16.5°C
Tomorrow's Minimum Temperature: 11.2°C
Tomorrow's Maximum Temperature: 18.7°C
Humidity: 72%
Wind Speed: 14.3 km/h
Wind Dominant Direction: 240
Weather Description: Partly cloudy
Is it Daytime? Yes
Daylight Duration: 10.25 hours
Sunshine Duration: 6.50 hours
Maximum UV Index is: 3.2
```

*Note: The example values are fictional and do not represent a live forecast.*

## 🔌 APIs Used

### Open-Meteo Geocoding API

Used to find a city's latitude and longitude from its name.

https://geocoding-api.open-meteo.com/v1/search

### Open-Meteo Forecast API

Used to retrieve current weather conditions and daily forecast information.

https://api.open-meteo.com/v1/forecast

Open-Meteo provides free access to its weather API for eligible non-commercial use without requiring an API key. Check its [official website](https://open-meteo.com/) for the latest usage terms.

## 📚 What I Learned

Through this project, I practiced:

- Defining and calling Python functions
- Working with dictionaries, lists, and tuples
- Sending HTTP requests with the `requests` library
- Using API parameters and query strings
- Parsing JSON responses
- Handling exceptions with `try` and `except`
- Checking data before accessing list elements
- Converting units and formatting output
- Organizing code into reusable functions

## 🔮 Future Improvements

Possible improvements for future versions include:

- Adding support for more weather codes
- Displaying wind direction using compass names, such as N, NE, and SW
- Improving error messages and input validation
- Adding a graphical user interface
- Supporting multiple cities in one session
- Adding more forecast days
- Writing automated tests

## 👨‍💻 Author

**MatinOfi**

GitHub: [@MatinOfi](https://github.com/MatinOfi)
