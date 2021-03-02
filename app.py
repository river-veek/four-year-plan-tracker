"""
--------------------------------------------------------------------------------
File containing the routing for application logic

Author: JT Kashuba
Group: TBD
Last Modified: 2/25/21
--------------------------------------------------------------------------------
"""
from __future__ import print_function # In python 2.7
from flask import Flask, render_template, abort, request, jsonify, json, redirect, url_for
import random
import sys


app = Flask(__name__)

# Dummy info for passing to html
names = ["951234567", "951234568", "951234569"]
terms = ["Fall", "Winter", "Spring", "Summer"]
years = ["1st", "2nd", "3rd", "4th", "5th"]
courses = ["CIS 210", "CIS 211", "CIS 212"]

# Starting with this class arrangement (by row instead of year) just to make it easier
# to make sure django code in the HTML is working (we can parse the python to match this if absolutely necessary)
forecast_rows = [
                [["CIS 210", "CIS 211", "CIS 212", ""],["CIS 110", "CIS 111", "CIS 199", ""]],
                [["CIS 313", "CIS 315", "CIS 425", ""],["CIS 314", "MATH 343", "CIS 471", ""]]
                ]

@app.route("/")
@app.route("/index", methods=['POST'])
def index():
    """
    Landing page
    """
    # Comment out the ui.html return statement and uncomment this to test the forecast page
    # Works with lists in the format of forecast_rows
    # return render_template('forecast.html', forecast_rows=forecast_rows)
    return render_template('ui.html', names=names, terms=terms, years=years, courses=courses)

# Going off JT's project creating route, including GET/POST methods 
@app.route("/forecast", methods=['POST'])
def forecast():
	"""
	Forecast page
	
	"""
	# using JSON to get data from form - gets string of list - needs to be passed to render_temp
	
	request_data = request.get_json()
	print(request_data, file=sys.stderr)
	print(request_data.keys(), file=sys.stderr)
	
	# only has one key
	tmp = request_data.keys()
	# will need to use to designate what button was called tableData - Save and display
	# savedData - Save button - will need global variable to contain all saved data and add each time most likely?
	if tmp[0] == 'login':
		print("LOGIN", file=sys.stderr)
		print("ID", request_data['login'], file=sys.stderr)
	if tmp[0] == 'tableData':
		# used for testing data transfer
		print("Clicked Save/Display", file=sys.stderr),
		print("Saved Classes: ", request_data['tableData'], file=sys.stderr)
		result = get_data(request_data)
		return render_template('forecast.html', forecast_rows=result)
	elif tmp[0] == 'savedData':
		print('Clicked Save', file=sys.stderr)
		print("Saved Classes: ", request_data['savedData'], file=sys.stderr)
	#prints to browser console it has been saved
	return "Saved Successfully"

def get_data(data):
	# print("IN GET DATA", data, file=sys.stderr)
	# print(len(data), file=sys.stderr)
	# needs to be formatted to correct list format for forecasting page
	arr = (data['tableData'])
	print(arr, file=sys.stderr)
	return arr

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

