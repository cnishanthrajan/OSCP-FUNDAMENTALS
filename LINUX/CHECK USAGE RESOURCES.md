[[OSCP-FUNDAMENTALS/LINUX/LINUX BASIC COMMANDS]]

#memory #diskusage #htop 

#free command to check the resources
![](IMAGES/image-6.png)


#memory 
#free free -m for more readable format
![](IMAGES/image-7.png)

#diskusage command is df
![](IMAGES/image-8.png)

you can see that everything is not easily understandable,
so we use the command df -h

![](IMAGES/image-9.png)

In a Linux Filesystem, we have two types of Disk usage one is via the space and the other one is the Inodes (WHICH IS THE MAXIMUM NUMBER OF FILES)

If either one is full, the files cannot be copied to that specific drive.

the command to check the inodes are full is by using > df -i
![](IMAGES/image-10.png)


#htop

command > htop

![](IMAGES/image-11.png)

#uptime command to check how long the system has been open or running

![](IMAGES/image-12.png)
