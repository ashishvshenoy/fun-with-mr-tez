#!/bin/bash
azure vm start group4 vm$1
azure vm reset-access -g group4 -n vm$1 -u ubuntu -p Ubuntu123$
ssh-keygen -R cs838fall2016group4$1.eastus.cloudapp.azure.com 
