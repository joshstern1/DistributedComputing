# EC601 Project: DistributedComputing

## Intro
Our product is a volunteer cloud that can safely host applications using volunteered resources, and those volunteering for resource usage. This is useful for business that need to run web functions without buying physical servers & individuals who need to make money from their CPU. We have chosen to implement a Function-as-a-Service (FaaS) infrastructure, because it allows jobs to only be running when they are requested by a client. Unlike AWS Lambda and other FaaS Providers, the our product offers serverless computing for lower costs and allows people to receive payment for volunteering their idle computers.

Our users are divided into 2 groups: lessees and lessors. Lessees would typically be small businesses for data research scientists, whereas lessors could be anyone with spare computing power. 

#### Minimal Viable Product
-Ability to run functions in the cloud<br/>
-Ability to volunteer a computer as a cloud node<br/>
-Auto-Scaling & Container Migration<br/>
-Easy to use interface


<img align="left" width="800" height="500" src="https://raw.githubusercontent.com/joshstern1/DistributedComputing/master/System%20Architecture.PNG"><br/>

## System Diagram Description
For those wanting to upload or run functions in the cloud, they would need to first connect to the central server. If they are uploading a function, the server would store it in a database. If they wish to run a function, the server will retrieve it from the database and offload the work to a volunteer node. When a volunteer node has completed a function, it will send the result back to the server, which will then give the result back to the client. We refer to these clients as lessors because they are paying for cloud resources. By implementing an FaaS infrastructure and running docker containers on the volunteer nodes, the server can just send the function code to the container rather than an entire virtual machine. This reduces the amount of data needing to be sent from several megabytes to a few kilobytes.


## Docker Containers
In our cloud, volunteers offer up their computers to run cloud jobs. We've chosen to use containers rather than virtual machines, due to how light containers are since they run in Linux and do not require a hypervisor. This gives us the ability to run more jobs on a volunteer worker with this extra space. We use docker containers that are responsible for receiving jobs from the master server, runing these jobs, and returning the output to the master server (which is actually serving as the client in this case).


## MySQL Database
We are using a MySQL database to store information about the users and the executables that the users want to run on the system. The database is connected with the Python server and the server can retrieve and set values in the database. How to install and run the MySQL database can be found in the database specific README.








