docker rm $(docker ps -a -q)
docker build -t course_planner .
docker run -d -p 5000:5000 course_planner
