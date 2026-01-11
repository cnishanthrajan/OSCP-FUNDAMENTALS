How to add a User 

Command > useradd -m neo 
![](IMAGES/20260111193928.png)
Here -m denotes that the Home Directory for the User will be created. If you don't put it, it wont create the Home Directory for that User. 

Here there are 4 users. We list it in the /home directory using ls -l command
![](IMAGES/20260111201119.png)

How to Lock a User
Command > usermod -L NEO
![](IMAGES/20260111201400.png)

How to check if a User is Locked
Command > passwd --status NEO
![](IMAGES/20260111201551.png)
Notice the L which is next to the user NEO it means that it is locked
Now the User will not get authenticated. 

How to check if an account is not expired.
Command> chage -l NEO
![](IMAGES/20260111202116.png)


Here we can see that Account Expires is never. This means that the account is Active. 


How to change the Default shell of the User from /bin/zsh to /bin/false (or) sbin/nologin
Command> usermod -s 
![](IMAGES/20260111202436.png)


How to check the User login access to the shell blocked.
Command> grep ^ NEO /etc/passwd
![](IMAGES/20260111202653.png)

We can see that the User NEO has no Login to the Shell which is zsh.

How to make the User account Expired.
Command > chage -E 2025-11-01 NEO
![](IMAGES/20260111203647.png)


How to check about the user if expired or not.
Command > chage -l NEO

![](IMAGES/20260111203817.png)

Now lets give access one by one to the User Neo by unlocking the User 
Command > usermod -U NEO
![](IMAGES/20260111204020.png)


Then Check the status of the Unlock. Here we can see the P. This means that the User is Unlocked.

![](IMAGES/20260111204137.png)


Now, Lets extend the expiry of the account

Command > chage -E 2028-12-30 NEO
![](IMAGES/20260111204432.png)

Check the Latest Expiry
![](IMAGES/20260111204506.png)


Now, lets make the User access the Shell so that the User NEO can access the Shell.

If you see when we try to change the USER to NEO using the command > su - NEO
It doesn't let us Login. 
![](IMAGES/20260111204707.png)


Check the shell status for NEO Command> Grep ^ NEO /etc/passwd
![](IMAGES/20260111204926.png)


Now lets give the access to the Shell to User NEO
Command > usermod -s /bin/zsh NEO
![](IMAGES/20260111205108.png)

Lets check the status now. 

![](IMAGES/20260111205216.png)


NEO has access now. Lets Login
![](IMAGES/20260111205245.png)


Success!!!

Enjoy!!