#!/bin/bash
# testHosts.sh

echo 'Opening File:' $1
for i in $(< $1)
do
	echo -e "\n=== ${i} ==="; \
	ssh -oStrictHostKeyChecking=no -i $2 ubuntu@${i} "hostname -i" ; \
	ssh -oStrictHostKeyChecking=no -i $2 ubuntu@${i} "hostname -f" ; \
done
