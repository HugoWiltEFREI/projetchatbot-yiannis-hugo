import os
#identifie un caractère spécial ou un retour à la ligne et renvoie True ou False
def identifySpeChr(car):
    if ((car>=' ' and car<='/')) or (car>=':' and car<='?') or (car>='[' and car<='`') or (car>='{' and car<='}') or car=='\n':
        return True
    else:
        return False

#pour 1 fichier discours la fonction crée son fichier de tokens dans le dossier cleaned
def createTokenFiles(nomDiscours):
    with open("speeches/{}".format(nomDiscours),"r",encoding=("utf8")) as f1, open("cleaned/cleaned_{}".format(nomDiscours[11:]),"w",encoding=("utf8")) as f2:
        inMot=False
        for car in f1.read():
            if identifySpeChr(car):
                if inMot==True:
                    f2.write('\n')
                    inMot=False
            else:
                inMot=traiterLettre(car,inMot,f2)
                
#créée pour diviser la fct createTokenFiles() en deux fonctions plus petites
def traiterLettre(car,inMot,f2):
    if car>='A' and car<='Z':
        f2.write(chr(ord(car)+ord('a')-ord('A')))
        inMot=True
    elif ord(car)>=192 and ord(car)<=220:
        f2.write(chr(ord(car)+ord('é')-ord('É')))
    else:
        f2.write(car)
        inMot=True
    return inMot
    
#remplie le dossier cleaned avec les fichier tokens de chaque fichier du dossier speeches                    
def createCleanedFolder():
    nomsDiscours=[]
    for nom in os.listdir("speeches"):
        if nom.endswith("txt"):
            nomsDiscours.append(nom)
    for nom in nomsDiscours:
        createTokenFiles(nom)
