## Doesn't work for REHL 7.0 7.1
## redhat 7
#!/bin/bash

echo "****************************"
echo "Starting Prepare Host"
echo "****************************"

echo -e "\nInstalling Packages"
sudo su
yum -y update

sudo yum install -y wget ntp

echo -e "\nSetting Umask to 022"
umask 022
echo "umask 022" >> ~/.bashrc
#change this to a sed statement

echo -e "\nSetting ulimit to 65535"
ulimit -n 65535

#disable SELinux
echo -e "\nDisabling SELinux"
sudo sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config

# Turn off autostart of iptables and ip6tables
echo -e "\nChecking firewalld is off"
sudo service firewalld stop
sudo chkconfig firewalld off

#Set Swapiness
echo -e "Setting Swapiness to 0"
sudo echo 0 | sudo tee /proc/sys/vm/swappiness
sudo echo vm.swappiness = 0 | sudo tee -a /etc/sysctl.conf

#Turn on NTPD
echo -e "Setting up NTPD and syncing time"
#Need to add a check to see if NTPD is installed.  If not install it
sudo chkconfig ntpd on
sudo ntpd -q
sudo service ntpd start

echo "Installing Oracle JDK7u79"
JDK_RPM="jdk7u79-linux-x64.rpm"
echo -e "JDK RPM: ${JDK_RPM}"
JDK_NAME="jdk1.7.0_79"
echo -e "JDK NAME: ${JDK_NAME}"
wget --no-check-certificate --no-cookies - --header "Cookie: oraclelicense=accept-securebackup-cookie" \
        -O $JDK_RPM http://download.oracle.com/otn-pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.rpm
chmod u+x $JDK_RPM
sudo rpm -ivh $JDK_RPM

#JDK_NAME="jdk1.7.0_79"
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

#Setup Disks
echo -e "Setting up Disks"
sudo mkfs -t ext4 /dev/xvdb
sudo mkfs -t ext4 /dev/xvdc
sudo cp /etc/fstab /etc/fstab.bak
sudo sed -i '$ a/dev/xvdb /data0 ext4 defaults 0 0' 	/etc/fstab
sudo sed -i '$ a/dev/xvdc /data1 ext4 defaults 0 0' 	/etc/fstab

echo -e "\n****************************"
echo "Prepare Nodes COMPLETE!"
echo "****************************"