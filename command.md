pip freeze > requirements.txt
chmod +x ./entrypoint.sh
http://0.0.0.0:8000/
docker-compose up -d --build
./manage.py startapp taskapp
docker exec -it django /bin/sh


<!-- carefull below command -->

To remove all containers (both running and stopped), you can use the following command:
--> docker-compose down
--> docker rm -f $(docker ps -aq)


To remove all images, you can use the following command:
docker rmi -f $(docker images -aq)
