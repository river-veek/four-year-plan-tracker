Author: JT Kashuba

Group: TBD

Members: JT Kashuba, Noah Kruss, Logan Levitre, Zeke Peterson, River Veek

Last Modified: 3/7/21

# CIS 422 - Project 2
# Four-Year Plan Tracker

## System Description

This system is a web application that provides functionality for processing, projecting,
and visualizing a Four-Year Plan for CIS Majors at UO. Ultimately this system can be
modularized to include all degree paths at UO, and theoretically any university (given
the time and resources to maintain this scale of implementation).

# Getting Started


## Install Instructions
Refer to (wherever we end up putting Install Instructions pdf)


## Software Dependencies

Docker (detail on how to install docker in Installation Instructions)

See requirements.txt for a full list of dependencies


## User Instructions

Refer to (wherever we end up putting User Instructions pdf)


## Repo Organization

* degree_logic - A directory containing files where objects are defined and instantiated
    * CIS_degree.py - A file containing the instantiated degree object containing all courses specific to the CIS Major
    * Gen_Ed.py - A file containing the instantiated degree object containing all general education courses
    * degree_objects.py - A file containing the definitions of the Degree, Course, and Term class objects
    * degree_planning.py - A file containing the functions used to generate a Four-Year Plan
    * student_objects.py - A file containing the definition of the Student class object
* pickles - A directory to hold the user's unique pickle files (essentially working as cookies)
    * tmp.txt - A placeholder file to maintain the pickle directory on the repo. Other files will populate this directory as the user creates Student objects using the website application
* static - Flask looks for the /static/ directory by default as the location where css and js files are stored
    * css - As mentioned above, Flask will default to looking in /static/css for all .css files
        * ui.css - A file containing the css for the website's UI
    * js - As mentioned above, Flask will default to looking in /static/js for all .js files
        * ui.js - A file containing the js for the website's UI
* templates - Flask looks for the /templates/ directory by default as the location where html files are stored
    * forecast.html - A file containing the html that displays on the webpage after the user clicks "Save & Display" to view their unique Four-Year Plan
    * ui.html - A file containing the landing page html
* testing - nosetests looks for the /testing/ directory by default as the location where files used for nosetests are stored
    * test_degree_objects.py - A file containing the nosetests to test the Degree object
    * test_generate_plan.py - A file containing the nosetests to test Degree planning logic
    * test_pickling.py - A file containing the nosetests to test pickled files
* Dockerfile - A standard Dockerfile used to build a docker container
* README.md - A brief overview of how to get started using this repo & the system therein
* app.py - A file containing the Flask routing and back end logic that populates the front end UI
* pickling.py - A file for saving and loading pickle objects
* requirements.txt - Document that denotes what libraries need to be imported by the user for the project to work (the user will not need to perform extra actions to import these libraries, building the docker container will automatically import the libraries contained in requirements.txt)
* run.sh - A bash script used to build and run the docker container in order to use the application via browser. Detailed steps on this process at the end of the "Docker" section below


## Docker

If you haven't used docker before, here are a couple useful tips to get started.

* List of docker containers running on your machine can be found using

  ```
  docker ps -a
  ```

* If a container is running and you want to delete it, first copy the container id found from executing the `docker ps -a` command and then use the following commands in order:


    * `docker kill <container_id>`

    * `docker rm <container_id>`

    * `docker images`

    * `docker rmi <image_id>`


If you aren't familiar with Dockerfile or bash scripts, make sure you use these command from inside the /tbd/ directory in order to avoid any start-up issues.

* Once you've deleted previous containers and images, use the following commands to build and run your new docker container (run.sh is included in the repo):

First, give `run.sh` r/w/e permissions by using the following command:

  ```
  chmod 777 run.sh
  ```

*Note: The command above MUST be used before using the run script*

Next, use the following command to build and run the Docker container:

  ```
  ./run.sh
  ```

* You will now be able to view and use the app! From a browser, enter the following URL:

  ```
  localhost:5000
  ```
