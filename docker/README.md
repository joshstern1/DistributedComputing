# Volunteer Node Container Using Docker
In our cloud, volunteers offer up their computers to run cloud jobs. To do this, we run docker containers on the volunteer nodes that can receive jobs from the master server, run these jobs, and return the output to the master server (which is actually serving as the client in this case).

## Installing Docker
The following instructions for installing docker were taken from https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04. We provide the necessary instructions for installation, but visit the link for more detailed information on installing docker.
```
sudo apt update

sudo apt install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

sudo apt update

sudo apt install docker-ce
```

## Using Docker
Docker containers are created from a basic image with layers added on top. These layers include installations and tools specific to the programs running within the container. Images are built using a Dockerfile, which specifies what needs to go into the container. Once a container image is built, the containers can be run, paused, resumed, or removed.
To create container:
```
docker build -t hello-world
```

To run container:
```
docker run -p 8000:8000 hello-world
```

To stop a container:
```
docker stop container-name
```
To remove a running container:
```
docker rm container-name
```
To remove a docker image:
```
docker rmi image-name
```
## Testing Docker
To test a client that uploads a function to the container:
```
python client.py (in a new terminal)
```
