import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to get APOD (Astronomy Picture of the Day) from NASA API
def get_apod_for_date(date=None):
    api_key = "DEMO_KEY"
    url = "https://api.nasa.gov/planetary/apod?api_key=" + api_key
    
    if date:
        url += f"&date={date}"  # Add the date parameter to the API request

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        image_url = data['url']
        description = data['explanation']
        date = data['date']
        copyright_info = data.get('copyright', 'No copyright info available')
        return image_url, description, date, copyright_info
    else:
        raise Exception(f"API request failed with status code {response.status_code}")

# Home route (display today's APOD)
@app.route('/')
def home():
    image_url, description, date, copyright_info = get_apod_for_date()
    return render_template('index.html', image_url=image_url, description=description, date=date, copyright_info=copyright_info)

# History route (display APOD for a specific date)
@app.route('/get_apod_by_date', methods=['GET'])
def history():
    date = request.args.get('date')  # Get the date from the query string
    if date:
        image_url, description, date, copyright_info = get_apod_for_date(date)
        return render_template('history.html', image_url=image_url, description=description, date=date, copyright_info=copyright_info)
    else:
        return "Error: No date provided", 400  # Handle case where no date is provided

if __name__ == '__main__':
    app.run(debug=True)
