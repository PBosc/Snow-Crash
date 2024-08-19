# Level 02

We got a pcap file which is an analytic of a tcp stream, let's analyze it in wireshark as a tck stream

We can see this was sent
``
Password: ft_wandr...NDRel.L0L
``

A quick hexdump show us that the dots correspond to character 127 which is the DEL character

Thus the user used the del key when on this dot so the password is `ft_waNDReL0L`

**Password** : `ft_waNDReL0L`

**Flag** : `kooda2puivaav1idi4f57q8iq`