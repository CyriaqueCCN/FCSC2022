# Nombre secret sur 16 octets ou 128 bits

Le programme distant nous dit si le nombre de bits à 1 du secret xor par le nombre à l'index i est pair ou impair. On écrit un script dans solve.py pour le résoudre et on récupère le flag

FCSC{e055ea6ffd540907c52a34bef47cbf79758e6732af597d98c33aceade78979c5}

## Explication de la méthode

On disopose de 136 nombres pour tester le secret, décomposés comme suit :

- envoyer n^0...n^127 bits pour chaque occurence du nombre (128 bits)
- envoyer 7 masques de contrôle pour faire une dichotomie et localiser l'erreur (7 bits)
- envoyer un nombre de parité pour vérifier que l'erreur ne se trouve pas dans les masques de contrôle (1 bit)

Les masques seront de la forme :

n1 = 00001111

n2 = 00110011

n3 = 01010101 etc

Avec le nombre de parité où tout est à 1 pour vérifier la cohérence entre les bits du secret et les masques de contrôle

n0 = 11111111

3 cas : 

- si erreur dans les 7 derniers : secret == odd(n0)
- si erreur dans n0 : secret != odd(n0)
- sinon, erreur dans secret : dichotomie

Dichotomie :

- bits\_at = [1, 2, 4, 8, 16] # 128 entiers, 1 pour chaque bit de la solution (STR !)
- e\_corr = [1111, 0011, 0101...] # 8 entiers de dichotomie (STR !)
- sec\_bits = [1, 0, 0, ... , 1, 0] # 128 entiers donnant le nombre secret avec erreur
- sec\_err = [1, 0, 1, 0, 0, 1, 1, 1] # 8 bits de dichotomie (int)
- sec\_orig = 188523174722555 # entier donnant le nombre secret avec erreur (si elle se trouve bien dans celui là)

```python
def get_error(sec_orig, e_corr, sec_err, i=0, chem=[]):
    # erreur dans moitié gauche ou droite
    if i > 6:
	return []
    else:
	if odd(sec_orig & e_corr[i]) == sec_err[i]: # erreur moitie gauche
	    return ['1'] + get_error(sec_orig, e_corr, sec_err, i+1)
	else:
	    return ['0'] + get_error(sec_orig, e_corr, sec_err, i+1)
	    # erreur moitié droite
```

Si erreur dans parité :

err\_idx vaudra forcément 127, donc :

- s pair -> parité 1, parité(so) 0, parité(so 127 inversé) 1
- s impair -> parité 0, parité(so) 1, parité(so 127 inversé) 0

Cette méthode fonctionne 135 fois sur 136 car elle ne peut pas détecter où se trouve l'erreur si celle-ci est sur le tout dernier bit. C'est largement suffisant pour passer les 32 tests consécutifs demandés pour obtenir le flag (environ 71% du temps) mais il y avait une méthode plus sûre : utiliser comme n0 (bit de contrôle total) non pas un entier initialisé à 11111...1111 mais un autre masque résultat des xors des 7 masques de contrôle n1-n7 : avec un tel masque, on peut comparer sa parité à celle des autres masques réunis : s'il y a une différence, c'est que l'erreur se situe dans un des 8 masques de contrôle. On ne peut la localiser mais on n'a alors plus à s'en soucier car ça signifie qu'elle ne se trouve pas dans le nombre secret, et donc qu'on peut l'afficher tel quel.
