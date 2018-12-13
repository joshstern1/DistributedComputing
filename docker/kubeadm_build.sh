#!/bin/bash
echo "starting kubernetes..."

#start up kubeadm
swapoff -a
kubeadm init --pod-network-cidr=192.168.0.0/16 > joining.txt

#runs these to start using cluster as regular user
mkdir -p $HOME/.kube
echo "Y" | cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config

#setup up CIDR
kubectl apply -f https://docs.projectcalico.org/v3.3/getting-started/kubernetes/installation/hosted/rbac-kdd.yaml
kubectl apply -f https://docs.projectcalico.org/v3.3/getting-started/kubernetes/installation/hosted/kubernetes-datastore/calico-networking/1.7/calico.yaml

#allow for pods to be scheduled on master node
kubectl taint nodes --all node-role.kubernetes.io/master-

#generate join.sh file that contains the command for adding worker nodes
./add_worker.py
