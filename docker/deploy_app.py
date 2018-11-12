import os
import time
try:

    os.system("kubectl run hello-world --image=gcr.io/api-project-vision/hello-world --port=8080")
    time.sleep(5)
    os.system('kubectl expose deployment/hello-world --type="NodePort" --port 8080')
    time.sleep(5)


    os.system("sudo kubectl get services/hello-world -o go-template='{{(index .spec.ports 0).nodePort}}' > out1.txt")
    os.system("sudo minikube ip > out2.txt")

except:
    print("Error starting service")
    exit(1)
