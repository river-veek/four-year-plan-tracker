"""
--------------------------------------------------------------------------------
File containing the routing for application logic

Author: JT Kashuba
Group: TBD
Last Modified: 2/15/21
--------------------------------------------------------------------------------
"""

from flask import Flask, render_template, abort, request
import random

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    """
    Landing page
    """
    return render_template('ui.html')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
