
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)
api_key = "7cfe5756ba3f5a06a762511733f63427" # Instructor

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/about')
def about():
    return "Thad Siwecki"

@app.route('/api/weather')
def weather():
    # get data from js request
    lat = request.json['lat']
    lon = request.json['lon']
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=imperial" % (
        lat, lon, api_key)
    
    

    # call openweather api
    response = requests.get(url)
    data = json.loads(response.text)
    return data

if __name__ == '__main__':
    app.run(debug=True)

