# quickWeather.py - Prints the weather for a location from the command line 
# (From "Automate the Boring Stuff With Python").

# TODO: Starting from 9 October 2015 Openweather API requires a valid APPID to retrieve data.
# Program needs to add APPID


import json, requests, sys

# Compute location from command line arguments.

if len(sys.argv) < 2:
	print('Usage: quickWeather.py location')
	sys.exit()
	
location = ''.join(sys.argv[1:])

# TODO: Download the JSON data from OpenWeatherMap.org's API.

url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()

# TODO: Load JSON data into a Python variable.

weatherData = json.loads(response.text)

# Print weather descriptions.

w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow: ')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow: ')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])