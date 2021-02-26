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

@app.route("/")
@app.route("/index")
def index():
    """
    Landing page
    """
    return render_template('ui.html', names=names, terms=terms, years=years, courses=courses)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
