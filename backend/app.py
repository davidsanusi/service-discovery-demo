# import all the required variables
from flask import Flask, escape, request, jsonify
import socket

# create an instance of the flask app
app = Flask(__name__)

# Housing data to be fetched
owners=["Alex","Kelvin","Cornelius","Mercy","Emmanuel","James","Margaret"]
color=["White","Red","Yellow","Blue","Pink"]
location=["Sydney","Cairo","Lagos","Budapest","Newcastle","Hamburg"]
buildingtype=["Duplex","Skyscrapper","Bunker","Bungalow"]


@app.route("/")
def index():
	return "Available routes are :'/owners','/color','/location','/type'"

@app.route("/owners")
def owners_of_Building():
    return jsonify({"data":owners,"ip":socket.gethostname()})

@app.route("/color")
def color_of_building():
    return jsonify({"data":color,"ip":socket.gethostname()})

@app.route("/location")
def location_of_building():
    return jsonify({"data":location,"ip":socket.gethostname()})

@app.route("/type")
def type_of_building():
    return jsonify({"data":buildingtype,"ip":socket.gethostname()})