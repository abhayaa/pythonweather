
from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
import requests

"""/Users/abhayabasnet/Desktop/Python/weatherBot.py"""

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    userInput = request.form['zip']

    condition = 1
    fahrenheit = 1
    city = 1
    iconCondition = " "

    if userInput.isdigit() == True:
        response= requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+userInput+',us&appid=fe22db5569ab3626316cda1a75a095a8')

        json_object = response.json()

        city = str.lower(json_object['name'])

        condition = str.lower(json_object['weather'][0]['main'])

        if condition == "clear":
            iconCondition = "cloudy1.png"
        if condition == "few clouds":
            iconCondition = "cloudy3.png"
        if condition == "shower rain":
            iconCondition = "shower3.png"
        if condition == "rain":
            iconCondition = "shower3.png"
        if condition == "thunderstorm":
            iconCondition = "tstorm2.png"
        if condition == "snow":
            iconCondition = "snow3.png"
        if condition == "mist":
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
        if condition == "few clouds":
            iconCondition = "cloudy3.png"
        if condition == "shower rain":
            iconCondition = "shower3.png"
        if condition == "rain":
            iconCondition = "shower3.png"
        if condition == "thunderstorm":
            iconCondition = "tstorm2.png"
        if condition == "snow":
            iconCondition = "snow3.png"
        if condition == "mist":
            iconCondition = "mist.png"

        kelvin = float(json_object['main']['temp'])

        fahrenheit = round((kelvin - 273.15) * 1.8 + 32)

    return render_template('temperature.html', temp=fahrenheit,city=city,cond=condition,icon=iconCondition)

@app.route('/')
def index():
    now = datetime.now()
    date = now.strftime('%m/%d/%Y')

    return render_template('index.html', date=date)


if __name__ == '__main__':
    app.run(debug=True)
