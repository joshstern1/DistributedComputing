To create container:
docker build -t hello-world .

To run container:
docker run -p 8000:8000 hello-world (first port # is on localhost, second port # is in the container)

To test a client that uploads a function to the container:
python client.py (in a new terminal)

To stop a container:
docker stop container-name

To remove a running container:
docker rm container-name

To remove a docker image:
docker rmi image-name
