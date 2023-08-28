pip freeze > requirements.txt
chmod +x ./entrypoint.sh
http://0.0.0.0:8000/

./manage.py startapp taskapp


<!-- docker container up and running -->
---> docker-compose up -d --build

<!-- opening files inside a container django is container name -->
docker exec -it django /bin/sh


<!-- carefull below command -->

To remove all containers (both running and stopped), you can use the following command:
--> docker-compose down
--> docker rm -f $(docker ps -aq)


To remove all images, you can use the following command:
docker rmi -f $(docker images -aq)


<!-- opening container files to use shell here django is container name --> 
docker exec -it django /bin/sh