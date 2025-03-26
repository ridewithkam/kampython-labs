import requests

def get_apod_for_date(date=None):
    api_key = "DEMO_KEY"
    url = "https://api.nasa.gov/planetary/apod?api_key=" + api_key
    
    if date:
        url += f"&date={date}"  # Add date parameter to the API request

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
