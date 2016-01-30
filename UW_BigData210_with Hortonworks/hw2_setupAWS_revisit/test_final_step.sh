#!/bin/bash

ssh -i evernote_NCalifornia.pem ec2-user@ec2-54-183-251-26.us-west-1.compute.amazonaws.com
echo "****************************"
echo "Starting Prepare Host"
echo "****************************"
echo "Copying prepareNodes.sh to nodes"


	#parallel-scp -l ec2-user -h cluster-hosts.txt -x "-oStrictHostKeyChecking=no -i /home/dave/keys/dpatton-1.pem" prepareNodes.sh /home/ec2-user/prepareNodes.sh
	pscp -v -l root -h cluster-hosts.txt -x " -oStrictHostKeyChecking=no -i evernote_NCalifornia.pem" prepareNode.sh /root/prepareNode.sh

	echo "Starting prepareNodes on each node"
	#parallel-ssh -t 0 -i -l ec2-user -h cluster-hosts.txt -x "-t -t -oStrictHostKeyChecking=no -i /home/dave/keys/dpatton-1.pem" 'chmod u+x prepareNodes.sh && ./prepareNodes.sh >> prepareNode.log && sudo reboot'
	pssh -v -t 0 -l root -h cluster-hosts.txt -x "-t -t -oStrictHostKeyChecking=no -i keys/id_rsa" 'chmod u+x prepareNodes.sh && ./prepareNodes.sh >> prepareNode.log && sudo reboot'
