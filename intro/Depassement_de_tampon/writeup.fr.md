Simple buffer overflow, on a une fonction shell à l'adresse 0x4011a2

La fonction main fait du bazar inutile puis nous demande une entrée. Elle lit 100 octets dans un buffer de 36 octets. Pour des raisons d'alignement, on va avoir RBP à RSP+48 et RIP à RSP+56, c'est notre offset. On écrit un petit script pwntools qui fait tout ça pour nous et on récupère le flag :

FCSC{5f25ae8fd59160b018e8ef21ff8972cdb2e3ab98e4f7bfced4e60255d378aee8}
