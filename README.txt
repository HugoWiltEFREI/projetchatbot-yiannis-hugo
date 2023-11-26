
███████ ███████ ██████  ███████ ██
██      ██      ██   ██ ██      ██
█████   █████   ██████  █████   ██
██      ██      ██   ██ ██      ██
███████ ██      ██   ██ ███████ ██
Membres du groupe : Yiannis LEBLANC, Hugo WILT
Lien vers le github : https://github.com/HugoWiltEFREI/projetchatbot-yiannis-hugo/tree/master

Fonctionnalités principales :
extractNomsPres (ou extraction dans menu):
Extraire les noms des présidents à partir des noms des fichiers texte fournis

associationTxtPrenomPres (ou association dans menu):
Associer à chaque président un prénom

list_of_files (ou liste dans menu):
Afficher la liste des noms des présidents

createCleanedFolder (ou nettoyage dans menu):
Nettoyage des fichiers (majuscule et ponctuation)

termFrequency (ou TF dans menu):
Prend en paramètre une chaine de caractères et qui retourne un dictionnaire associant à chaque mot le nombre de fois qu’il apparait dans la chaine de caractères

dicoIDF (ou IDF dans menu):
Prend en paramètre le répertoire où se trouve l’ensemble des fichiers du corpus et qui retourne un dictionnaire associant à chaque mot son score IDF

TF-IDF:
prend en paramètre le répertoire où se trouvent les fichiers à analyser et qui retourne la matrice TF-IDF

programmes:
Fonctions qui permet d'exécuter toutes les fonctions dans : Fonctionnalités à développer
->uselessWordsList renvoie les mots avec un score TF-IDF de 0
->rareWordsList renvoie les mots avec un score TF-IDF > val (permet de choisir le degré de rareté)
->motImportantDiscours mot le plus répété par un président (en utilisant la fonction addition si le président à fais plusieurs discours)
->motDit renvoie les discours dans lesquels le mot est présent avec le nombre d'occurrence et le président ayant dit le mot le plus de fois
->firstOccurrence renvoie le premier président à avoir dit le mot
->recurrentWordsList Mots que tous les présidents ont évoques (hormis non importants)

help:
Imprime le fichier README.txt

plot:
Plot un graph qui montre le nombre d'occurrence de chaque mots supérieurs à val pour chaque documents du directory
