# Level 00

```bash
level00@SnowCrash:~$ ls -la
total 12
dr-xr-x---+ 1 level00 level00  100 Mar  5  2016 .
d--x--x--x  1 root    users    340 Aug 30  2015 ..
-r-xr-x---+ 1 level00 level00  220 Apr  3  2012 .bash_logout
-r-xr-x---+ 1 level00 level00 3518 Aug 30  2015 .bashrc
-r-xr-x---+ 1 level00 level00  675 Apr  3  2012 .profile
```

There is nothing to work with

We look for everything owned by the flag00 user to see if we can get anything

```bash
level00@SnowCrash:~$ find / -user flag00 2>/dev/null
/usr/sbin/john
/rofs/usr/sbin/john
```
```bash
level00@SnowCrash:~$ cat /usr/sbin/john
cdiiddwpgswtgt
```

Looks like Cesaro encode string

cdiiddwpgswtgt => nottoohardhere

Looks like a password

**Password** : `nottoohardhere`

**Flag** : `x24ti5gi3x0ol2eh4esiuxias`