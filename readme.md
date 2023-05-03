# Overview

This project is the implementation of a weather app for various locations.

You can start the web server by using the command:
>`python3 manage.py runserver`

I built this app to learn django, and to learn bootstrap 4 styling.

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

index.html - this page is the starting page. It asks the user to provide a location. Once a location has been provided, it retrieves weather data (temp, wind speed, current conditions) and location data (map, current time at this location) and displays it. It also provides a way for you to 'save' this location and provides a link to a status page.

city_list.html - this page pulls from local storage all the locations that you care about, then retrieves current weather data on each of them, and displays the data as cards. It provides a way to remove locations, and to go back to the index page to search for additional locations.

# Development Environment

I used VS Code, Django 3, Python 3.9 and Bootstrap 4 to build this project.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
* [Django](https://www.djangoproject.com/)
* [RealPython Django Tutorial](https://realpython.com/get-started-with-django-1/)

# Future Work

* Resizing the index.html page to a narrow width causes scroll bars to appear around the map iframe, and it looks janky. 
* Cards are not always the same height when a long name for the city appears.
