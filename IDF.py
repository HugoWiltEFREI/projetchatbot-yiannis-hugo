import os
from math import log10

def nombreOccurrence(chaineDeC): #On définie la fct nombreOccurrence avec comme argument chaine de caractère
    nombreOcc = dict()  #On créer un dico vide où l'on va stocker le nombre d'occurrence des mots dans la chaine
    listeDeMots = chaineDeC.split() #On délimite les mots en regardant où sont les espaces et on les stocks dans un liste
    for mots in listeDeMots:
        if mots in nombreOcc:
            nombreOcc[mots] += 1 #Si le mot est déjà dans le dico, on fait +1
        else:
            nombreOcc[mots] = 1 #Sinon on rajoute le mot dans le dico avec la valeur 1
    return nombreOcc

#La fonction renvoie un tuple des noms de chaque fichier du dossier directory
def getCleanedFilesNames(directory):
    list=[]
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            list.append(file)
    return tuple(list)

def dicoIDF(directory):
    dicoMots={}
    nbFichier=0
    for discours in getCleanedFilesNames(directory):
        nbFichier+=1
        with open("{}/{}".format(directory,discours),'r',encoding="utf8") as file:
            setMots=set()
            for mot in file.read().split():
                if not(mot in setMots):
                    setMots.add(mot)
                    if mot in dicoMots.keys():
                        dicoMots[mot]+=1
                    else:
                        dicoMots[mot]=1
    for mot in dicoMots.keys():
        dicoMots[mot]=log10(nbFichier/dicoMots[mot])
    return dicoMots

print(dicoIDF("cleaned"))
