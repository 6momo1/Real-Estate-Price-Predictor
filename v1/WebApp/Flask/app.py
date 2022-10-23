from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
# from flask_sqlalchemy import SQLAlchemy
# google api
import googlemaps
from datetime import datetime
from pprint import pprint


gmaps = googlemaps.Client(key='KEY')

def location_info(location):
    location = location + 'Vancouver, Canada'
    try:
        geocode_result = gmaps.geocode(location)

        north = geocode_result[0]['geometry']['bounds']['northeast']['lat']
        east = geocode_result[0]['geometry']['bounds']['northeast']['lng']
        south = geocode_result[0]['geometry']['bounds']['southwest']['lat']
        west = geocode_result[0]['geometry']['bounds']['southwest']['lng']

        location = geocode_result[0]['geometry']['location']

        bound = { 'north':north, 'east':east, 'south':south, 'west':west }

        dic = { 'bound':bound , 'location':location }
        return dic

    except Exception as e: print(e)
        


app = Flask(__name__)


@app.route("/",methods = ['GET', 'POST'])
def home():
    data = {
            'location': { 'lat': 49.250005, 'lng': -123.138127 }, 
    }

    if request.method == 'POST':
        location = request.form['location']
        if location:
            data = location_info(location)
            print(data)
            return render_template('index.html',data=data,location=location)

    else:
        return render_template('index.html',data=data,location='Please select a location')





if __name__ == "__main__":
    app.run(debug=True)