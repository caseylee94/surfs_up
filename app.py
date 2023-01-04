# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#    return'Hello world'

# Import all dependencies
import datetime as dt
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Set up the database engine
engine = create_engine("sqlite:///hawaii.sqlite")

# # Reflect the database into the engine
Base = automap_base()

# Reflect tha tables
Base.prepare(engine, reflect=True)

# # Create the variables to access the measurement and station databases
Measurement = Base.classes.measurement
Station = Base.classes.station

# #Create a session link
session = Session(engine)

# #Create the flask app
app = Flask(__name__)

# # Define the welcome route
@app.route("/")

# Create the function the display the weather variables
def welcome():
    return(
    '''
    <br>
    Welcome to the Climate Analysis API!
    </br> <br>
    Available Routes:
    </br> <br>
        /api/v1.0/precipitation
    </br> <br>
        /api/v1.0/stations
    </br> <br>
        /api/v1.0/tobs
    </br> <br>
        /api/v1.0/temp/start/end
    </br>
    ''')



# Create the app for precipitation data
@app.route("/api/v1.0/precipitation")

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)


# Create the route for the stations data
@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)



# Create the route for the temperature observations
@app.route("/api/v1.0/tobs")


def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


# Create the route for the statistical data

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)