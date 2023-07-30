# Weather-forecast-WebApp

Weather App
------
The Weather App is a web application that allows users to get live weather data for a particular location. Users can search for a city, and the app will display the current weather information, including description, temperature, humidity, and feels like.

Features
--
* User Registration and Login: Users can register and log in to the application to access personalized features.
* Live Weather Data: The app uses the OpenWeatherMap API to fetch real-time weather data for a given location.
* Data Storage: Weather data is stored in a MySQL database, allowing users to access previously searched weather information.

Tech Stack
--
The Weather App is built using the following technologies:

* Python 3.10.8
* Django 4.1.3: Python web framework
* Django REST framework: For API views
* MySQL: Database to store weather data
* HTML, CSS: Frontend user interface
* OpenWeatherMap API: External weather data provider

Usage
---
* Register a new account or log in if you already have one.
* On the homepage, enter a city name in the search box and click "Search" to get the live weather data for that location.
* The app will display the weather description, temperature in both Kelvin and Celsius, humidity, and feels-like temperature.
* Previously searched locations and weather data are saved in the database and can be accessed on the dashboard.

Note
--
You have to change the API key as well as MySql connwctions while runing the server. 
