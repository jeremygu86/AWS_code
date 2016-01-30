# prepare all nodes
#!/bin/bash

for i in $(cat nodeIPs.txt)
do
    echo "=== ${i} ==="
    echo "++ upload key file ++"
    scp -i ./node/JamesUW.pem ./node/JamesUW.pem ec2-user@${i}:"\/home\/ec2-user/JamesUW.pem"
    echo "++ set permission ++"
    ssh -i ./node/JamesUW.pem ec2-user@${i} "chmod 600 /home/ec2-user/JamesUW.pem"
    echo "++ upload hosts file ++"
    scp -i ./node/JamesUW.pem ./node/hosts ec2-user@${i}:"\/home\/ec2-user"
    echo "++ replace hosts file ++"
    ssh -t -i ./node/JamesUW.pem ec2-user@${i} "sudo cp /etc/hosts /etc/hosts.bak; sudo cp ~/hosts /etc/hosts";
    echo "++ upload prepare script ++"
    scp -i ./node/JamesUW.pem ./node/doSetup.sh ec2-user@${i}:"\/home\/ec2-user\/doSetup.sh"
    echo "++ set permission for setup script ++"
    ssh -i ./node/JamesUW.pem ec2-user@${i} "chmod +x /home/ec2-user/doSetup.sh"
    echo "++ please run setup script from each node ++"
done

