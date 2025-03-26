from flask import Flask, render_template, request
from apod import get_apod_for_date  # Import model function

app = Flask(__name__)

@app.route('/')
def home():
    # Get APOD for today's date 
    image_url, description, date, copyright_info = get_apod_for_date()
    return render_template('index.html', image_url=image_url, description=description, date=date, copyright_info=copyright_info)

@app.route('/get_apod_by_date', methods=['GET'])
def history():
    # Get the date entered by the user from the query parameter
    date = request.args.get('date')  
    
    if date:
        # If a date is provided, use it to grab the APOD for date
        image_url, description, date, copyright_info = get_apod_for_date(date)
    else:
        # If no date is provided, use today's date by default
        image_url, description, date, copyright_info = get_apod_for_date()

    return render_template('history.html', image_url=image_url, description=description, date=date, copyright_info=copyright_info)

if __name__ == '__main__':
    app.run(debug=True)
