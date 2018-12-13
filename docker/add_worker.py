#!/usr/bin/env python

import os
f1 = open("joining.txt", "r")
cmd = ""
for line in f1:
    if "kubeadm join" in line:
        cmd = line

f1.close()
i = 0
while True:
    if cmd[i] != 'k':
        i = i + 1
    else:
        break

f2 = open("join.sh", "w")
cmd = cmd[i:len(cmd)-1]
f2.write("#!/bin/bash")
f2.write("\n\n")
f2.write(cmd)
f2.close()
