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
@app.route("/index")
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
	# using JSON to get data from form - gets Array - needs to be passed to render_temp
	if request.method == 'POST':
		request_data = request.get_json()
		
		# print("GOT POST", file=sys.stderr)
		# Print Functions are seen in Container logs
		# print(type(request_data), file=sys.stderr)
		
		# output Dictionary of {'tData': list of lists
		# Disregard u in front of each index - stands for Unibit - goes away
		# print(request_data['tdata'], file=sys.stderr)
		
		# shows it is a list	
		#print(type(request_data['tdata']),file=sys.stderr)
				
		# get List of lists - used to pass into forecast
		result = get_data(request_data)
		
	# Not needed as of now but possibly later
	elif request.method == 'GET':
		print("Get", file=sys.stderr)

	return render_template('forecast.html', forecast_rows=result)

def get_data(data):
	# print("IN GET DATA", data, file=sys.stderr)
	# print(len(data), file=sys.stderr)
	arr = (data['tdata'])
	print(arr, file=sys.stderr)
	return arr

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

