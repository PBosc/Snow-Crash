# Level 01

```bash
level01@SnowCrash:~$ ls -la
total 12
dr-x------ 1 level01 level01  100 Mar  5  2016 .
d--x--x--x 1 root    users    340 Aug 30  2015 ..
-r-x------ 1 level01 level01  220 Apr  3  2012 .bash_logout
-r-x------ 1 level01 level01 3518 Aug 30  2015 .bashrc
-r-x------ 1 level01 level01  675 Apr  3  2012 .profile
level01@SnowCrash:~$ find / -user flag01 2>/dev/null
level01@SnowCrash:~$
```

This time we do not have anything

We want to connect to flag01, let's check the /etc/passwd file to see if we can get something usable

```bash
level01@SnowCrash:~$ cat /etc/passwd
...
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
...
```

The flag01 is the only user to have its password in this file let's try to decrypt it using john on a kali docker container

```
docker run --rm --privileged --mount type=bind,source=/home/pibosc/Desktop/Projects/Snow-Crash/level01/ressources,target=/data --name tmp -it kalilinux/kali-last-release
```

```
apt-get update
apt-get upgrade
apt-get install john
john data/passwd
john --show
abcdefg
```

We found the password

**Password** : `abcdefg`

**Flag:** `f2av5il02puano7naaf6adaaf`
