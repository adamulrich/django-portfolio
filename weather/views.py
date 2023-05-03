from django.shortcuts import render
import requests
from datetime import datetime, timedelta
from dotenv import dotenv_values

# constants
config = dotenv_values()
WEATHER_KEY = config['WEATHER_KEY']
MAP_KEY = config['MAP_KEY']
URL = 'https://api.openweathermap.org/data/2.5/weather'
COOKIE_CITIES = 'cities'

# this function retrieves weather data and a map for the requested city.
# input:  city (string)
# output: weather object
def get_weather_data(city):

    PARAMS = {'q':city ,
            'appid': WEATHER_KEY,
            'units': 'imperial'}

    # if the city is an integer, we are parsing a list
    # in this case, we need to change the param to id: instead of q:
    try:
        int(city)
        PARAMS = {'id':city ,
            'appid': WEATHER_KEY,
            'cnt': 1,
            'units': 'imperial'}
    except:
        pass

    # get weather data
    req = requests.get(url=URL, params=PARAMS)
    # if weather is successful
    if req.status_code ==  200:

        # get the json, and retrieve the data.
        weather_data = req.json()

        current_city_name = weather_data['name']
        lat = weather_data['coord']['lat']
        lon = weather_data['coord']['lon']
        current_country_name = weather_data['sys']['country']
        current_city_id = weather_data['id']
        current_temp = round(weather_data['main']['temp'] * 10) / 10
        current_wind_speed = round(weather_data['wind']['speed'] * 10) / 10
        current_description = weather_data['weather'][0]['description']
        current_icon = weather_data['weather'][0]['icon']
        d:datetime = datetime.utcnow()
        
        current_time = (d + timedelta(seconds=weather_data['timezone'])).strftime('%a %b %d, %Y %H:%M')
        
        map_height=300
        map_width=700
        map_zoom=9
        current_icon_url = f'https://openweathermap.org/img/wn/{current_icon}@4x.png'
        bing_map =  f'https://dev.virtualearth.net/REST/V1/Imagery/Map/Road/{lat},{lon}/{map_zoom}?pushpin={lat},{lon};37&mapSize={map_width},{map_height}&key={MAP_KEY}'

        # set up the object to pass it back to the render
        weather_object = {'city': current_city_name, 
                        'lat': lat,
                        'lon': lon,
                        'current_temp': current_temp,
                        'current_wind_speed': current_wind_speed,
                        'current_description': current_description,
                        'current_icon_url': current_icon_url,
                        'current_city_name': current_city_name,
                        'current_country_name': current_country_name,
                        'current_city_id': current_city_id,
                        'current_time': current_time,
                        'date': datetime.today(),
                        'bing_map': bing_map}

        return weather_object

    else:
        return

# this function gets the value from a POST if available, gathers weather and location data, and renders index.html
def index(request):

    weather_object = {}

    # get the city name from the form post
    if 'city' in request.POST:
        city = request.POST['city']
        if city != '' :
            # get weather data
            weather_object = get_weather_data(city)
   
    # call the render
    return render(request, 'weather/index.html', weather_object )

# this function retrieves the current cookie and uses it to generate weather data from the location list
# it then renders the city_list.html page.
def list(request):

    # get cookie for city ids
    city_ids = request.COOKIES.get(COOKIE_CITIES)
    cities = city_ids.split(",")
    if cities == ['']:
        cities = []

    #create object
    weather_object_list = []

    #walk the city list
    for city in cities:
        # get weather data
        weather_object_list.append(get_weather_data(city)) 

    context = {
        'cities': weather_object_list
    }
    
    #call the render
    return render(request, 'weather/city_list.html', context )
