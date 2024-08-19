# Level 13

This exercice is about modifying register while a program is running to spoof our UID using gdb.

`gdb ./level13`
<br>
`layout asm`
<br>
`b getuid` Stop a getuid call
<br>
`run`
<br>
`step`
<br>
`step`
<br>
`set $eax=0x1092` Replace the call result
<br>
`step`

**Flag:** `2A31L79asukciNyi8uppkEuSx`
