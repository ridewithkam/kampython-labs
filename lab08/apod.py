import requests

def get_apod_for_date(date=None):
    api_key = "i3WRVMMGvuHovaOvajheBWu54OY5EaTJSs1vpmWX"
  
    
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    if date:
        url += f"&date={date}"  

    # Make request to NASA API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # get data from the response
        image_url = data.get('url', '')
        description = data.get('explanation', '')
        date = data.get('date', date)  # Use provided date if available
        copyright_info = data.get('copyright', 'No copyright info available')

        return image_url, description, date, copyright_info
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
