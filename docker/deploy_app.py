import os
import time
try:

    os.system("kubectl run hello-demo --image=gcr.io/api-project-vision/hello-demo --port=8080")
    time.sleep(5)
    os.system('kubectl expose deployment/hello-demo --type="ClusterIP" --port 8080')
    time.sleep(5)

    os.system("sudo kubectl get services/hello-demo -o go-template='{{(index .spec.clusterIP)}}' > out1.txt")


except:
    print("Error starting service")
    exit(1)
