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
--------------------------------------------------------------------------------
Refer to (wherever we end up putting Install Instructions pdf)


## Software Dependencies
--------------------------------------------------------------------------------
Docker (detail on how to install docker in Installation Instructions)

See requirements.txt for a full list of dependencies


## User Instructions
--------------------------------------------------------------------------------
Refer to (wherever we end up putting User Instructions pdf)


## Repo Organization
--------------------------------------------------------------------------------



## Docker
--------------------------------------------------------------------------------
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
