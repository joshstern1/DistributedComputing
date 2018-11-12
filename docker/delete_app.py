import os

try:
    cmd = "kubectl delete service hello-world"
    os.system(cmd)
    cmd = "kubectl delete deployment hello-world"
    os.system(cmd)
except:
    print("Error deleting service")
    exit(1)
