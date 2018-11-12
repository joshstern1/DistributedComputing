# Volunteer Node Container Using Docker and Kubernetes
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
docker build -t hello-world .
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

## Installing Minikube and Kubectl
Install kubectl:
```
sudo apt-get update && sudo apt-get install -y apt-transport-https
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubectl
```

Install Minikube:
```
curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.30.0/minikube-linux-amd64 && chmod +x minikube && sudo cp minikube /usr/local/bin/ && rm minikube
```

##Using Kubernetes
Start Minikube cluster:
```
sudo minikube start
```

Create Deployment:
```
sudo kubectl run hello-world --image
```
