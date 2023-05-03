from django.shortcuts import render
import requests
from datetime import datetime, timedelta

API_KEY = "b254a5652f0594f0e3d3c9ce8bef5d5e"
URL = 'https://api.openweathermap.org/data/2.5/weather'
COOKIE_CITIES = 'cities'

def get_weather_data(city):

    # current_city_name = 'City name not found. Please include only the city name, not state or zip code.'
    # lat = ''
    # lon = ''
    # current_country_name = ''
    # current_city_id = ''
    # current_temp = ''
    # current_wind_speed = ''
    # current_description = ''
    # current_icon = ''
    # current_icon_url = ''
    # bing_map = ''

    PARAMS = {'q':city ,
            'appid': API_KEY,
            'units': 'imperial'}

    try:
        int(city)
        PARAMS = {'id':city ,
            'appid': API_KEY,
            'cnt': 1,
            'units': 'imperial'}
    except:
        pass

    # get weather data
    req = requests.get(url=URL, params=PARAMS)
    if req.status_code ==  200:
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
        print(current_time)
        key = 'Am27Bsy1tM3G4a6CQZ10Sva7FaKgzsg527w_RB1M0TtB288Fnc99KfCmAm3TAFr0'
        current_icon_url = f'https://openweathermap.org/img/wn/{current_icon}@4x.png'
        bing_map =  f'https://dev.virtualearth.net/REST/V1/Imagery/Map/Road/{lat},{lon}/8?pushpin={lat},{lon};37&mapSize=300,300&key=Am27Bsy1tM3G4a6CQZ10Sva7FaKgzsg527w_RB1M0TtB288Fnc99KfCmAm3TAFr0'

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

# Create your views here.
def index(request):

    city = ''
    current_city_name = 'Enter a city name to see the current weather'
    lat = ''
    lon = ''
    current_country_name = ''
    current_city_id = ''
    current_temp = ''
    current_wind_speed = ''
    current_description = ''
    current_icon = ''
    current_icon_url = ''
    current_time = ''
    bing_map = ''


    weather_object = {'city': city, 
        'lat': lat,
        'lon': lon,
        'current_temp': current_temp,
        'current_wind_speed': current_wind_speed,
        'current_description': current_description,
        'current_icon_url': current_icon_url,
        'current_city_name': current_city_name,
        'current_country_name': current_country_name,
        'current_city_id': current_city_id,
        "current_time": current_time,
        'date': datetime.today(),
        'bing_map': bing_map}


    # get the city name from the form post
    if 'city' in request.POST:
        city = request.POST['city']
        if city != '' :

            weather_object = get_weather_data(city)
        
            print(weather_object)

    
    # call the render
    return render(request, 'weather/index.html', weather_object )


def list(request):

    # get cookie for city ids
    city_ids = request.COOKIES.get(COOKIE_CITIES)
    cities = city_ids.split(",")
    if cities == ['']:
        cities = []

    #create object
    weather_object_list = []

    print(cities)
    for city in cities:
        print(city)
        weather_object_list.append(get_weather_data(city)) 

    print(weather_object_list)
    context = {
        'cities': weather_object_list
    }
    
    return render(request, 'weather/city_list.html', context )

