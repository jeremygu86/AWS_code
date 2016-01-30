# BASICS How Docker Works with Chinese Notes :)

Docker is a client-server application. Docker Host --> Docker Clinet + Server (including Containers) 

1. The Docker server is a daemon that does all the heavy lifting: building and downloading images, starting and stopping containers, and the like. 

It exposes a REST API for remote management.

2. The Docker client is a command line program that communicates with the Docker server using the REST API. 

You will interact with Docker by using the client to send commands to the server.

3. The machine running the Docker server is called the Docker host. 

The host can be any machine—your laptop, a server in the Cloud™, etc—but, because Docker uses features only available to Linux, that machine must be running Linux (more specifically, the Linux kernel).


在安装之前了解一些概念

当我们在一台 Linux 主机上安装完 Docker 之后，我们的机器中就包含了本地主机和 Docker 主机。如果从网络层来划分，本地主机就代表你的电脑，而 Docker 主机就代表你运行的容器。

在一个典型的 Linux 主机上安装 Docker 客户端，运行 Docker daemon ，并且在本地主机上直接运行一些容器。这就意味着你可以为 Docker 容器指定本地主机端口，例如 localhost:8000 或者 0.0.0.0:8376。

linux_docker_host

在 OS X 上安装的 Docker ， docker 进程是通过 Boot2Docker 在 Linux 虚拟主机上运行的。

mac_docker_host

在 OS X 中，Docker 主机地址就是 Linux 虚拟主机地址。当你启动 boot2docker 进程的时候，虚拟主机就会为它指定IP。在 boot2docker 下运行的容器，通过端口映射的方式将端口映射到虚拟主机上。你可以通过本页面上的操作实践来体会到这一点。


# INSTALLATION
英文：https://viget.com/extend/how-to-use-docker-on-os-x-the-missing-guide
中文：http://wiki.jikexueyuan.com/project/docker/examples/mongodb.html

Step 1: Install VirtualBox
Step 2: Install Docker and boot2docker
> brew update
> brew install docker
> brew install boot2docker

Step 3: Initialize and start boot2docker

boot2docker init
boot2docker up
    export DOCKER_HOST=tcp://192.168.59.103:2376
    export DOCKER_CERT_PATH=/Users/wenxiaogu/.boot2docker/certs/boot2docker-vm
    export DOCKER_TLS_VERIFY=1
    
    
装好后每次运行下面命令
----------------------------
Step 4: Set the DOCKER_HOST environment variable
Your VM might have a different IP address—use whatever boot2docker up told you to use. You probably want to add that environment variable to your shell config.
 
Step 5: Profit
docker info
# 


1. 常用Docker命令：
https://gitlab0.bigdata220uw.mooo.com/jhenri/uwbd-instructions/blob/spark_tutorial_class3/Running%20Docker.md

2. 小试牛刀：
https://gitlab0.bigdata220uw.mooo.com/jhenri/uwbd-instructions/blob/master/Docker%20Demo%201.md

3. Running Docker on Spark
https://gitlab0.bigdata220uw.mooo.com/jhenri/uwbd-instructions/blob/master/Running%20Dockerized%20Spark.md
以下是开始运作


常用Docker命令：
## Page Conventions

| Component | The name of the one on this page |
|---|---|
| docker-engine VM, aka <BR> docker-machine VM, aka <BR> container host, aka <BR> docker VM | vm0 |
| container | sandbox1 |

## Step1. Provisioning a docker-engine VM

To create a docker-engine VM using virtualbox and default parameters:

    docker-machine create --driver virtualbox vm0

To destroy a docker-engine VM:

    docker-machine rm vm0
To list all vms
docker-machine ls


ls -lh
docker ps
Provisioning time is the only time when you can change the VM parameters through docker-machine.  Fortunately, the usual ways of working with docker make reprovisioning an easy operation.

Here is an example allocating 4GB of RAM, 20GB of disk, and 4 cores:

    docker-machine create --driver virtualbox --engine-opt dns=8.8.8.8 --virtualbox-cpu-count=4 --virtualbox-memory=4096 --virtualbox-disk-size=20000 vm0

## Rebooting the docker-engine VM
    docker-machine stop vm0
    docker-machine start vm0

## Reprovisioning the docker-engine VM
    docker-machine kill vm0
    docker-machine rm vm0
    docker-machine create vm0 [arguments for create]

## Step2. Connecting to the container terminal with ssh and docker-enter instead of docker exec or docker run:
启动container：2. 小试牛刀
docker-machine start {VM name}

Started machines may have new IP addresses. You may need to re-run the `docker-machine env` command.
docker-machine env   {VM name}


For more information
echo $DOCKER_HOST
docker ps
cd ~/.docker 所在的目录


2.1. 建立第一个container
docker run -it ubuntu:trusty bash 并自动连进去


新开一个窗口
eval $(docker-machine env  {VM name})
docker ps
可以看到刚才开的那个打开了
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS               NAMES
91180ac9964d        ubuntu:trusty       "bash"              About a minute ago   Up About a minute                       naughty_boyd


停止并删除 mysite 容器。
$ docker stop mysite
$ docker rm mysite  

https://geraldkaszuba.com/quickly-ssh-into-a-docker-container/

2.2. 建立第2个container
Initialize your environment with docker-machine env.

Start a container called sandbox1:
给容器挂载一个卷
    docker run -v /usr/local/bin:/target jpetazzo/nsenter
    docker-enter sandbox1
    
2.3. 建立第三个容器
非常好的资源：http://wiki.jikexueyuan.com/project/docker/installation/mac.html
docker run -d -P --name web nginx
一般来说，docker run 命令会启动一个容器，运行这个容器，然后退出。-d 标识可以让容器在 docker run 命令完成之后继续在后台运行。 -P 标识会将容器的端口暴露给主机，这样你就可以从你的 MAC 上访问它。


启动一个新的 nginx 容器,并将本地的 site 目录替换容器中的 html 文件夹。
$ docker run -d -P -v $HOME/site:/usr/share/nginx/html --name mysite nginx


2.4 建立第四个容器（pyspark：https://gitlab0.bigdata220uw.mooo.com/jhenri/uwbd-instructions/blob/master/Running%20Dockerized%20Spark.md）

docker run -it -p 8088:8088 -p 8042:8042 --name sandbox1 sequenceiq/spark:1.6.0 bash


## Troubleshooting

#### Troubleshooting: Pyspark hang
    root@c3d628813a19:/# pyspark
      [hang . . .]

You are likely out of memory.  The boot2docker "default" machine only has 2GB.  Make sure you passed the --virtualbox-memory and set at least 3072 (MB).  Less than 3GB is unlikely to work well.

As a point of reference, the sequenceiq spark 1.6 container, with default settings, with pyspark loaded, but without any real work done, measures 2.6GB according to top:

    top - 16:28:50 up 11 min,  0 users,  load average: 0.30, 0.67, 0.43
    Tasks:  13 total,   1 running,  12 sleeping,   0 stopped,   0 zombie
    Cpu(s):  0.4%us,  0.0%sy,  0.0%ni, 99.6%id,  0.0%wa,  0.0%hi,  0.0%si,  0.0%st
    Mem:   3079384k total,  2605436k used,   473948k free,    62484k buffers


#### Troubleshooting: message about regenerating certs

    $ eval $(docker-machine env dev)
    Error checking TLS connection: Error checking and/or regenerating the certs: There was an error validating certificates for host "192.168.99.101:2376": x509: certificate is valid for 192.168.99.100, not 192.168.99.101
    You can attempt to regenerate them using 'docker-machine regenerate-certs [name]'.
    Be advised that this will trigger a Docker daemon restart which will stop running containers.

This happens if you restart your docker-machine and virtualbox decides to give you a new ip address.  To secure the docker protocol with https, docker-machine generates a self-signed SSL certificate, which is tied to an IP.  When this happens, take the advice of the error:

    docker-machine regenerate-certs dev
    eval $(docker-machine env dev)

#### Troubleshooting: DNS problems

##### DNS problems, an example:
    docker run -it -p 8088:8088 -p 8042:8042 --name sandbox1
    sequenceiq/spark:1.6.0 bash
    Error response from daemon: no such id: sandbox1
    Error: failed to remove containers: [sandbox1]
    Unable to find image 'sequenceiq/spark:1.6.0' locally
    Pulling repository docker.io/sequenceiq/spark
    Network timed out while trying to connect to https://index.docker.io/v1/reposito
    ries/sequenceiq/spark/images. You may want to check your internet connection or
    if you are behind a proxy.

##### DNS problems, testing

To test DNS:
    curl http://www.google.com -o google_home.html

As a response to the curl test, errors about connections and names are bad.  This is good:
```
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100  151k    0  151k    0     0  1399k      0 --:--:-- --:--:-- --:--:-- 1643k
```

##### DNS problems, fix

Takes time, but should resolve DNS issues, at least within the container.  Destroy your docker-machine VM and recreate, being sure to include the flag:

    --engine-opt dns=8.8.8.8

##### DNS problems, workaround 1

Faster.  SSH to the docker-machine (not the container).  Then:

    echo "nameserver 8.8.8.8" > /etc/resolv.conf

Now restart your containers.

##### DNS problems, workaround 2

Fast but temporary.

Restart the docker machine.
