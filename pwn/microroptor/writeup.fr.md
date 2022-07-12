ELF 64 bits, strippé. Au temps pour les symboles. On a la totale niveau protection, excepté le canary. On va donc probablement avoir un buffer overflow suivi d'un ROP ou d'un ret2libc.

On décompile un coup (dans source.c) : effectivement, on lit 512 octets dans un buffer[32]. Avant ça, le programme nous donne gentiment l'adresse d'une des chaînes hardcodées dans le binaire. On peut donc l'utiliser pour trouver l'offset du PIE.

Cependant, il va nous falloir 2 phases, une fois calculé l'offset : d'abord trouver la libc (ce qu'on fait avec un gadget trouvé avec ropper et en utilisant le PLT et le GOT) puis une fois dans la libc trouver la chaîne /bin/sh et system.

On utilise une fois encore pwntools. On crée 2 ropchains, la première leakant la libc et la seconde exécutant notre shell. On accole l'adresse de main à la fin de la première pour obtenir une réentrance et pouvoir envoyer la seconde.

```
$ ./solve.py
[+] Starting local process './microroptor': pid 83068
[*] Switching to interactive mode
0x55b1e54db010
Nope, you are no master.
$ whoami
syca
```

Ok, ça marche en local ! Maintenant on va essayer en remote.

Coup de bol, ça marche du premier coup ! Je m'attendais à devoir leak les fonctions de la libc pour en trouver la version avec libc.blukat.me mais on dirait que j'ai la même que le serveur (ou en tout cas qu'il n'y a pas eu de décalage avant l'offset qui m'intéresse)

FCSC{e3752da07f2c9e3a0f9ad69679792e5a8d53ba717a2652e29fb975fcf36f9258}
