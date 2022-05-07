from django.shortcuts import render
from django.views import View
from django.conf import settings
import requests

# Create your views here.
class MainPage(View):
    def get(self, request, *args, **kwargs):
        city = request.GET.get('city', 'Manila')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.API_KEY}"
        data = requests.get(url).json()
       
        payload = {
            'city': data['name'],
            'weather': data['weather'][0]['main'],
            'icon': data['weather'][0]['icon'],
            'fahrenheit_temperature': round((data['main']['temp'] - 273.15) * (9/5) + 32, 2),
            'celsius_temperature': round(data['main']['temp'] - 273.15, 2),
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }

        if payload['city'].find('City') == -1:
            payload['city'] = payload['city'] + ' City'
 
        context = {
            'data': payload
        }

        print(round(payload['fahrenheit_temperature'], 2))

        return render(request, "forecast/home.html", context)
