"""
--------------------------------------------------------------------------------
File containing the routing for application logic

Author: JT Kashuba
Group: TBD
Last Modified: 2/25/21
--------------------------------------------------------------------------------
"""

from flask import Flask, render_template, abort, request
import random

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
    # return render_template('forecast.html', forecast_rows=forecast_rows)
    return render_template('ui.html', names=names, terms=terms, years=years, courses=courses)

# Need another app route for generating the forecast matrix, currently using index for testing

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
