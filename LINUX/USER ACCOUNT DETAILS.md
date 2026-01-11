 #etc/passwd  #etc/shadow #LockUserAccounts  #CheckUserAccountBlocked #usergroups 

This Topic Explains the below mentioned things.
1. /etc/shadow --> What's Inside the File.  #etc/shadow 
2. /etc/passwd --> What's inside the File. #etc/passwd 
3. How to Lock a User #LockUserAccounts 
4. How to Check if a User is Locked #CheckUserAccountBlocked 
5. User groups information #usergroups 

It is important to know how Linux stores User and Group account details. 

There are Two Authentication schemes in Linux -
1. /etc/passwd
2. /etc/shadow

/etc/passwd --> info about user accounts are stored in /etc/passwd file
/etc/shadow --> passwords of all users are stored in /etc/shadow file

/etc/passwd can be read by anyone. The reason if map Username to User ID. This is the reason why fingerprint of the passwords are stored in /etc/shadow file. 


/etc/passwd can be accessed only with high privileges.

#etc/shadow 
```
root:$6$pfiZTzNB1wav3OFG$GDwbvI44D7sBuX7Q.6LmNWx.RaU6nzxZWCCkkMNIXCkvANnNoYogV983NSLkG1cfpaW4mmyFuTOKkDf53hVkh/:18781:0:99999:7:::
```
The above is content of an /etc/shadow file. 

Lets examine the contents and understand what they mean.

Each part is separated by a colon.
1. The Root entry is the username in plain text.
2. The next piece which is quite long represents encryption password.
3. The next field 18781 which represents the last-time password was changed, in Timestamp format. 
4. 0 is the minimum number of days required between password changes.
5. 99999 represents the maximum number of days the password is valid for.
6. 7 represents the number of days in advance of the password expiration date in which the user will be warned that they need to change the password.

#etc/passwd 
Now lets examine the contents of /etc/passwd file.

```
john:x:1002:1002:John Doe,,,:/home/john:/bin/bash
```

1. john is the username in plain text.
2. x indicates that the password needs to be pulled from the shadow file.
3. The first 1002 indicates the UID (User ID), unique number on the system for each user in the system.
4. The second 1002 indicates the Primary Group ID (GID) the User belongs to.
5. The next John Doe is the Comment Field called the Optional Field which is used to store the general information about the user like the full name, address etc.
6. Next the /home/john contains the Users Home Directory location.
7. /bin/bash is the Default Shell Environment for the User. 

#LockUserAccounts
It is Important to Note that the UID of 0 is always assigned to a System Administrator Superuser called Root. It is possible to assign the UID of 0 to other users but it is highly not recommended because of Security Concerns.

USER Accounts can be Disabled and Enabled in several ways.

**1st Method**
1st Method to Lock a USER is by using the below two commands. 

1. usermod -L username
2. passwd -l username

This places an (!) in front of the Password Hash in the /etc/shadow file.  This can be applied manually to the File also. 

Now when the particular locked user tries to authenticate password. The Authentication method will fail for the particular User.


**2nd Method**

Another method is to Mark the User Account as Expired by setting the Expiry Date which is the 8th Field of the /etc/shadow file. We use the **Command** >**chage -E**
We can mention a back date of the current date so that the User Account becomes expired. 

**3rd Method**

The Third method is to change the default shell of the USER in the etc/passwd file to /bin/false (or) sbin/nologin. 

/bin/false will Exit immediately. 
/sbin/nologin will display the message the account is currently not available. 

We can use the **command > usermod -s** to change the default shell of the particular user which we want to lock. 


#CheckUserAccountBlocked 

What if we want to know if a User account is Locker

If we would like to know whether a user account is disabled or locked, we have to verify all three methods mentioned above. We can use the following commands to check for expiration dates, password-locks, and non-interactive shells.

1. command > passwd --status jane 

```
root@kali:~# passwd --status jane
jane L 03/15/2021 0 99999 7 -1

root@kali:~# chage -l jane
Last password change                                    : Mar 15, 2021
Password expires                                        : never
Password inactive                                       : never
Account expires                                         : never
Minimum number of days between password change          : 0
Maximum number of days between password change          : 99999
Number of days of warning before password expires       : 7
```

We can see from the above that Jane's Password is Locked.

2. command > chage -l

   We then used chage -l to confirm that the account is not expired.

3. command > grep ^ jane /etc/passwd
```
root@kali:~# grep ^jane /etc/passwd
jane:x:5001:5001::/home/jane:/sbin/nologin
```

We use grep with a regular expression to find a line that begins with "jane". Grep returned jane's properties in /etc/passwd, where we can verify that the default shell is /sbin/nologin. This means that login access for the account is disabled.


#usergroups
USER GROUPS
 Information about user groups are stored in the /etc/group file. Let's review an example entry of this file. 
``````
bluetooth:x:117:kali
``````

1. bluetooth  - bluetooth is the group name,
2. x - group password (usually not used),
3. 117 is the group ID
4. kali is a particular user that belongs to the specified group

Note that only users who have a secondary group membership are listed in /etc/group, since primary group memberships are stored in /etc/passwd.
