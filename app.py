from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None

    if request.method == 'POST':
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        past_days = request.form['past_days']
        weather_data = get_weather_data(latitude, longitude, past_days)

    return render_template('index.html', weather_data=weather_data, zip=zip)

def get_weather_data(latitude, longitude, past_days):
    api_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&past_days={past_days}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
    
    response = requests.get(api_url)
    weather_data = response.json()

    return weather_data['hourly']

if __name__ == '__main__':
    app.run(debug=True)
