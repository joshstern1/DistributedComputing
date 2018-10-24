# DistributedComputing
BU ENG EC 601 Project

## Intro
Our product is a volunteer cloud that can safely host applications using volunteered resources, and reimburse owners for resource usage. This is useful for business that need to run web functions without buying physical servers & individuals who need to make money from their CPU. Unlike AWS Lambda and other FaaS Providers, the our product offers serverless computing for lower costs and allows people to receive payment for volunteering their idle computers.

Our users are divided into 2 groups: lessees and lessors. Lessees would typically be small businesses for data research scientists, whereas lessors could be anyone with spare computing power. 

### Minimal Viable Product
-Ability to run functions in the cloud<br/>
-Ability to volunteer a computer as a cloud node<br/>
-Auto-Scaling & Container Migration<br/>
-Easy to use interface

## Docker
In our cloud, volunteers offer up their computers to run cloud jobs. To do this, we run docker containers on the volunteer nodes that can receive jobs from the master server, run these jobs, and return the output to the master server (which is actually serving as the client in this case).


Docker provides “Operating System-Level Virtualization”<br/>
Runs on isolated Linux container<br/>
More lightweight than a VM (no hypervisor)<br/>
Created from basic “images” by adding layers on top





