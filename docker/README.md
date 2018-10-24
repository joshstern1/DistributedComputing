# Volunteer Node Container Using Docker

## Installing Docker
The following instructions for installing docker were taken from https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04
We provide the necessary instructions for installation, but more detailed information on installing docker at this link.

https://github.com/joshstern1/DistributedComputing/blob/9c31cd1c5611e906d6af275bf0b1dda73b5c4f1a/docker/docker_installation.txt#L1-L6


## Using Docker
To stop a container:
docker stop container-name

To remove a running container:
docker rm container-name

To remove a docker image:
docker rmi image-name

## Testing Docker
To test a client that uploads a function to the container:
python client.py (in a new terminal)
