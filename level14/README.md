# Level14

This exercice is about modifying register while getflag command is running to spoof our UID using gdb.

`gdb ./level13`
<br>
`layout asm`
<br>
`b ptrace`
<br>
`b getuid`
<br>
`run`
<br>
`step`
<br>
`set $eax=0`
<br>
`step`
<br>
`step`
<br>
`set $eax=3014`
<br>
`step`

**Flag:** `7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ`
