from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = {}
    if request.method == 'POST':
        city = request.form['city']
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            current = data['current_condition'][0]
            weather = {
                'city': city.title(),
                'temperature': current['temp_C'],
                'description': current['weatherDesc'][0]['value'],
                'humidity': current['humidity']
            }
        else:
            weather = {'error': 'Could not retrieve weather info.'}
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
