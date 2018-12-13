import os
import time
try:
    
    #delete the kubernetes service and deployment after a function is completed
    cmd = "kubectl delete service hello-demo"
    os.system(cmd)
    cmd = "kubectl delete deployment hello-demo"
    os.system(cmd)
except:
    print("Error deleting service")
    exit(1)
