# FCSC 2022 - Writeups

> Stands for [French CyberSecurity Challenge](https://www.ssi.gouv.fr/agence/cybersecurite/france-cybersecurity-challenge-2022/) by the [ANSSI](https://www.ssi.gouv.fr/) (National Agency for the Security of Information Systems).
> Its goal was to select two teams of youngsters to tackle the ECSC, an european CTF. I was a year too old to be eligible but participation was open to anyone.

### Writeups

I threw here all the notes I took during the challenges, sorry for the format and less-than-stellar explanations of the challenges.

Most of the writeups are in english but I rewrote some of them in french to help french-speakers who asked for a solution at the end of the CTF.

Some of the cool ones :

##### [XoraaS](pwn/XORaaS/writeup.fr.md)

Binary exploitation challenge : Overwrite the last byte of RBP with an off-by-one buffer overflow to push a controled address on RIP

##### [microroptor](pwn/microroptor/writeup.fr.md)

Binary exploitation challenge : Defeat PIE and ASLR with a leaked function pointer using ROP and ret2plt

##### [Guess me too](misc/Guess_me_too/writeup.fr.md)

Programming challenge : a "guess the number" with a limited amounts of bits of information where the server had the right to lie once when answering.
