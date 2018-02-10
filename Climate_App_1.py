from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")
print("Connected to DB")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
print("Reflected tables")


# Create our session (link) from Python to the DB
session = Session(engine)

# Save reference to the table
# Measurement = Base.classes.measurement
# Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
# Define all api routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation - List of precipitation by date<br/>"

        f"/api/v1.0/stations"
        f"- List of stations<br/>"

        f"//api/v1.0/tobs"
        f"- List of temperature observations for the last year<br/>"

        f"/api/v1.0/<start> and /api/v1.0/<start>/<end>"
        f"- a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.<br/>"
    )

@app.route("/api/v1.0/tobs")
def measurements():
    """ Return a list of all temperature observations for the last year 
    """
    # Query all measurements
    results = session.query(Measurement.date, Measurement.tobs).all()
   
    # Convert list of tuples into normal list
    all_temps = [record.tobs for record in results]

# Create a dictionary from the row data and append to a list of all_measurements
    all_measurements = []
    for temp in all_temps:
        measurement_dict = {}
        measurement_dict["date"] = Measurement.date
        measurement_dict["Temp"] = Measurement.tobs
        all_measurements.append(measurement_dict)

    return jsonify(all_measurements)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations"""
    # Query all stations
    results = session.query(Measurement.station).all()

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of precipitation"""
    # Query all stations
    results = session.query(Measurement.prcp).all()

   
if __name__ == '__main__':
    app.run(debug=True)
