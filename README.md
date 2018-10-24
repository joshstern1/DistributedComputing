# EC601 Project: DistributedComputing

## Intro
Our product is a volunteer cloud that can safely host applications using volunteered resources, and those volunteering for resource usage. This is useful for business that need to run web functions without buying physical servers & individuals who need to make money from their CPU. Unlike AWS Lambda and other FaaS Providers, the our product offers serverless computing for lower costs and allows people to receive payment for volunteering their idle computers.

Our users are divided into 2 groups: lessees and lessors. Lessees would typically be small businesses for data research scientists, whereas lessors could be anyone with spare computing power. 

#### Minimal Viable Product
-Ability to run functions in the cloud<br/>
-Ability to volunteer a computer as a cloud node<br/>
-Auto-Scaling & Container Migration<br/>
-Easy to use interface

<img align="left" width="400" height="600" src="https://raw.githubusercontent.com/joshstern1/DistributedComputing/master/System%20Architecture.PNG">

## Docker
In our cloud, volunteers offer up their computers to run cloud jobs. We've chosen to use containers rather than virtual machines, due to how light containers are since they run in Linux and do not require a hypervisor. This gives us the ability to run more jobs on a volunteer worker with this extra space. We use docker containers that are responsible for receiving jobs from the master server, runing these jobs, and returning the output to the master server (which is actually serving as the client in this case).

Docker containers are created from basic “images” by adding layers on top. 


## MySQL Database
We are using a MySQL database to store information about the users and the executables that the users want to run on the system. The database is connected with the Python server and the server can retrieve and set values in the database. How to install and run the MySQL database can be found in the database specific README.








