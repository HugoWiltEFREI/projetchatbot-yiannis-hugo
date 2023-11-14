import os

def identifySpeChr(car): #fonction qui détermine si un caractère est un catère spécial ou nom et renvoie un boulleen
    if ((car>=' ' and car<='/')) or (car>=':' and car<='?') or (car>='[' and car<='`') or (car>='{' and car<='}') or car=='\n':
        return True
    else:
        return False
    
def createTokenFiles(nomDiscours): #ouvre un fichier discours et créer un fichier nettoyé ; encodage des fichier en utf-8 pour les accents (pas sûr de l'utilité pour le ficher en mode "read"
    with open("speeches/{}".format(nomDiscours),"r",encoding=("utf8")) as f1, open("cleaned/cleaned_{}".format(nomDiscours[11:]),"w",encoding=("utf8")) as f2:
        inMot=False # nous ne savons pas en ouvrant le fichier si le 1er carac et une lettre, en affectant False au bool nous évitons de sauter une ligne
        for car in f1.read():#pour chaque caractère du fichier on détermine si c'est un lettre ou un caractère spécial
            if identifySpeChr(car #si le caractère que nous lisons et un caractère spécial nous stopons l'écriture dans le fichier cleaned et sautons une ligne
                if inMot==True: #afin de ne pas sauter plusieurs ligne (ex: retour à la ligne + trait d'union + espace etc) nous vérifions que nous nous trouvions dans le mot
                    f2.write('\n')# et seulement dans le cas ci-dessus nous sautons une ligne, dans le cas contraire on ne fait rien
                    inMot=False
            else: # si le caractère lu est une lettre alors il faut l'écrire au format minuscule
                if car>='A' and car<='Z': # si c'est une majuscule nous avançons vers sa version miscule dans le tableau ascii
                    f2.write(chr(ord(car)+ord('a')-ord('A')))
                    inMot=True
                elif ord(car)>=192 and ord(car)<=220: # si c'est une majuscule accentuée nous faisons de même
                    f2.write(chr(ord(car)+ord('é')-ord('É')))
                else:
                    f2.write(car) # si c'est une minuscule nous l'écrivons telle quelle
                    inMot=True # le bool inMot vérifie que notre curseur  se trouve dans un mot (réelle utilité du bool plus haut)
def fillCleanedFolder(): # fonction de regroupement qui crée et rempli automatiquement le dossier cleaned à partir du dossier discours (qui doit être dans le répertoire local du fichier d'exécution)
    nomsDiscours=[]
    for nom in os.listdir("speeches"):
        if nom.endswith("txt"):
            nomsDiscours.append(nom)
    for nom in nomsDiscours:
        createTokenFiles(nom)
