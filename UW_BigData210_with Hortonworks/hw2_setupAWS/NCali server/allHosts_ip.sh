#!/bin/bash

echo 'Opening File:' $1
for i in $(< $1)
do
        echo "=== ${i} ==="
        
        ssh -t -oStrictHostKeyChecking=no -i $2 ec2-user@${i} "hostname -f"; \
        scp -oStrictHostKeyChecking=no -i $2 hosts ec2-user@${i}:hosts; \
        ssh -t -oStrictHostKeyChecking=no -i $2 ec2-user@${i} "sudo cp /etc/hosts /etc/hosts.bak; sudo cp ~/hosts /etc/hosts"; \
done