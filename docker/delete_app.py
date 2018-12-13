import os
import time
try:
    time.sleep(3)
    cmd = "kubectl delete service hello-demo"
    os.system(cmd)
    cmd = "kubectl delete deployment hello-demo"
    os.system(cmd)
except:
    print("Error deleting service")
    exit(1)
