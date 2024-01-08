from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None

    if request.method == 'POST':
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        weather_data = get_weather_data(latitude, longitude, start_date, end_date)

    return render_template('index.html', weather_data=weather_data)

def get_weather_data(latitude, longitude, start_date, end_date):
    api_url = f'https://archive-api.open-meteo.com/v1/era5?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&hourly=temperature_2m'
    
    response = requests.get(api_url)
    weather_data = response.json()

    return weather_data['hourly']

if __name__ == '__main__':
    app.run(debug=True)
