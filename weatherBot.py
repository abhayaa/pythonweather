
from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
import requests



app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    userInput = request.form['zip']
'''
Initializes the conditions to use in the following code
'''

    condition = 1
    fahrenheit = 1
    city = 1
    iconCondition = " "
'''
Detects if the user input is a Zipcode or a City and does the following processes:
    Gets the response from the openweathermap API, and converts the JSON data into the specifics:
        *city
        *weather condition - takes the result returned from this returns the appropriate image
        *temperature - takes the kelvin temperature that is returned and converts to fahrenheit
        *assigns each returned value to a value to return in the HTML page.
    Once all the necessary data is collected, it is sent to the appropriate place for display within the html
'''


    if userInput.isdigit() == True:
        response= requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+userInput+',us&appid=fe22db5569ab3626316cda1a75a095a8')

        json_object = response.json()

        city = str.lower(json_object['name'])

        condition = str.lower(json_object['weather'][0]['main'])

        if condition == "clear":
            iconCondition = "cloudy1.png"
        elif condition == "few clouds":
            iconCondition = "cloudy3.png"
        elif condition == "shower rain":
            iconCondition = "shower3.png"
        elif condition == "rain":
            iconCondition = "shower3.png"
        elif condition == "thunderstorm":
            iconCondition = "tstorm2.png"
        elif condition == "snow":
            iconCondition = "snow3.png"
        elif condition == "mist":
            iconCondition = "mist.png"
        kelvin = float(json_object['main']['temp'])
        fahrenheit = round((kelvin - 273.15) * 1.8 + 32)

    elif userInput.isdigit() == False:
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+userInput+',us&appid=cbccdccb44cb0e84dfa9c6d9444a209a')

        json_object = response.json()

        city = str.lower(json_object['name'])

        condition = str.lower(json_object['weather'][0]['main'])


        if condition == "clear":
            iconCondition = "cloudy1.png"
        elif condition == "few clouds":
            iconCondition = "cloudy3.png"
        elif condition == "shower rain":
            iconCondition = "shower3.png"
        elif condition == "rain":
            iconCondition = "shower3.png"
        elif condition == "thunderstorm":
            iconCondition = "tstorm2.png"
        elif condition == "snow":
            iconCondition = "snow3.png"
        elif condition == "mist":
            iconCondition = "mist.png"

        kelvin = float(json_object['main']['temp'])

        fahrenheit = round((kelvin - 273.15) * 1.8 + 32)

    return render_template('temperature.html', temp=fahrenheit,city=city,cond=condition,icon=iconCondition)
'''
routes the page to the index page where the location is collected
'''
@app.route('/')


    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
