#!/bin/bash

echo "****************************"
echo "Starting Prepare Host"
echo "****************************"

sudo su

echo -e "\nSetting Umask to 022"
umask 022
## sometimes single quote works. vi ~/.bashrc
echo "umask 022" >> ~/.bashrc

#disable SELinux
echo -e "\nDisabling SELinux"
sudo sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config

# Turn off autostart of iptables and ip6tables
echo -e "\nChecking ipTables and ip6table are off"
sudo service iptables stop
sudo chkconfig iptables off
sudo service ip6tables stop
sudo chkconfig ip6tables off


#Set Swapiness
echo -e "Setting Swapiness to 0"
echo 0 | sudo tee /proc/sys/vm/swappiness
echo vm.swappiness = 0 | sudo tee -a /etc/sysctl.conf

#Turn on NTPD
echo "Setting up NTPD and syncing time"
#Need to add a check to see if NTPD is installed.  If not install it
sudo chkconfig ntpd on
sudo ntpd -q
sudo service ntpd start


# gwx: note that the mnt is in xvdb or xvdc. use lsblk to figure it out.
lsblk 

sudo mkfs -t ext4 /dev/xvdc # not the mnt one


sudo mkfs -t ext4 /dev/xvdd
sudo mkfs -t ext4 /dev/xvde


sudo mv /var/log /var/log-original
sudo mkdir /var/log /data0 /data1

sudo cp /etc/fstab /etc/fstab.bak

sudo sed -i '$ a/dev/xvdc /var/log ext4 defaults 0 0' 	/etc/fstab


sudo sed -i '$ a/dev/xvdd /data0 ext4 defaults,noatime 0 0' /etc/fstab
sudo sed -i '$ a/dev/xvde /data1 ext4 defaults,noatime 0 0' /etc/fstab

sudo mount –o remount /data1, /data2


#Install Oracle JDK 7
########################################################################
# NOTE: YOU MAY NEED TO UPDATE THE URL FOPR A MORE RECENT JDK VERSION
########################################################################
echo "Installing Oracle JDK7u79"
JDK_RPM="jdk7u79-linux-x64.rpm"
echo "JDK NAME:" $JDK_NAME
wget --no-check-certificate --no-cookies - --header "Cookie: oraclelicense=accept-securebackup-cookie" \
        -O $JDK_RPM http://download.oracle.com/otn-pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.rpm
chmod u+x $JDK_RPM
rpm -ivh $JDK_RPM

JDK_NAME="jdk1.7.0_79"
export JDK_HOME="/usr/java/${JDK_NAME}"
echo "SETTING JDK_HOME TO: " $JDK_HOME

sudo alternatives --install /usr/bin/java java /usr/java/${JDK_NAME}/jre/bin/java 20000
sudo alternatives --install /usr/bin/jar jar /usr/java/${JDK_NAME}/bin/jar 20000
sudo alternatives --install /usr/bin/javac javac /usr/java/${JDK_NAME}/bin/javac 20000
sudo alternatives --install /usr/bin/javaws javaws /usr/java/${JDK_NAME}/jre/bin/javaws 20000
sudo alternatives --set java /usr/java/${JDK_NAME}/jre/bin/java
sudo alternatives --set javaws /usr/java/${JDK_NAME}/jre/bin/javaws
sudo alternatives --set javac /usr/java/${JDK_NAME}/bin/javac
sudo alternatives --set jar /usr/java/${JDK_NAME}/bin/jar

ls -lA /etc/alternatives/{jar,java*}
java -version

echo -e "\n****************************"
echo "Prepare Nodes COMPLETE!"
echo "****************************"



### 
sudo chkconfig --level 345 ncsd on
sudo ncsd -g


echo sudo hdfs – nofile 32768 >> /etc/security/limits.conf
echo sudo mapred – nofile 32768 >> /etc/security/limits.conf
echo sudo hbase – nofile 32768 >> /etc/security/limits.conf
echo sudo hdfs – nproc 32768 >> /etc/security/limits.conf
echo sudo mapred – nofile 32768 >> /etc/security/limits.conf
echo sudo hbase – nofile 32768 >> /etc/security/limits.conf

## don't reboot
## sudo reboot



