--------------------------------------------------------------------------------
Author: JT Kashuba
Group: TBD
Last Modified: 2/15/21
--------------------------------------------------------------------------------

# Getting Started

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


If you aren't familiar with Dockerfile or bash scripts, make sure you use the next command from inside the /tbd/ directory in order to avoid any start-up issues.

* Once you've deleted previous containers and images, use the following command to build and run your new docker container (run.sh is included in the repo):

  ```
  ./run.sh
  ```

* You will now be able to view the app! From a browser, enter the following URL:

  ```
  localhost:5000
  ```
