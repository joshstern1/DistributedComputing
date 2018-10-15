To create container:
docker build -t hello-world .

To run container:
docker run -p 8000:8000 hello-world

To test a client that uploads a function to the container:
python client.py (in a new terminal)
