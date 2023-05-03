# Overview

This django app retrieves and displays weather, map and time data for user selected locations.

# Prerequisities
Before running this code, you need to install django and python-dotenv
>`pip install django`

>`pip install python-dotenv`

You will also need to provide keys - WEATHER_KEY and MAP_KEY (OpenWeatherAPI KEY and Bing Maps key) in a 
.env file in the weather folder.
<code><br><br>
WEATHER_KEY=<br>
MAP_KEY=<br>
</code>

# Startup
You can start the web server by using the command:
>`python3 manage.py runserver`

I built this app to learn django, and to learn bootstrap 4 styling.

[Software Demo Video](https://youtu.be/ghFcAGNvzbw)

# Web Pages

index.html - this page is the starting page. It asks the user to provide a location. Once a location has been provided, it retrieves weather data (temp, wind speed, current conditions) and location data (map, current time at this location) from OpenWeatherApi and Bing Maps and displays it. Because many places have the same name, a map is provided to ensure that you have the correct location. It also provides a way for you to 'save' this location using a cookie, and provides a link to a status page.

city_list.html - this page pulls from a cookie all the locations that you have saved, then retrieves current weather data on each of them, and displays the data as cards. It provides a way to remove locations, and to go back to the index page to search for additional locations.

# Development Environment

To build this project, I used VS Code with Python 3.9.13. Libraries included are Bootstrap 4 and Python-Dotenv. Web Services used are Bing Maps and OpenWeatherAPI.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
* [Django](https://www.djangoproject.com/)
* [RealPython Django Tutorial](https://realpython.com/get-started-with-django-1/)
* [OpenWeatherAPI](https://openweathermap.org/api)
* [Bing Maps](https://learn.microsoft.com/en-us/bingmaps/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)

# Future Work

* ~~Resizing the index.html page to a narrow width causes scroll bars to appear around the map iframe, and it looks janky.~~
* ~~no favicon~~ 
* Cards are not always the same height when a long name for the city appears.
