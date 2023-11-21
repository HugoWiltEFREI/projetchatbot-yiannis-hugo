from math import log10
dico = {}

from fonctions import creerListe


def nombreOccurrence(chaineDeC): #On définie la fct nombreOccurrence avec comme argument chaine de caractère
    nombreOcc = dict()  #On créer un dico vide où l'on va stocker le nombre d'occurrence des mots dans la chaine
    listeDeMots = chaineDeC.split() #On délimite les mots en regardant où sont les espaces et on les stocks dans un liste
    for mots in listeDeMots:
        if mots in nombreOcc:
            nombreOcc[mots] += 1 #Si le mot est déjà dans le dico, on fait +1
        else:
            nombreOcc[mots] = 1 #Sinon on rajoute le mot dans le dico avec la valeur 1
    return nombreOcc

def nombreDeMots(dictionnaire):
    total = sum(dictionnaire.values())
    return total

def pourcentage(dico): #A changer pour effectuer calcul sur dico et pas texte
    dicoPourcent = {}
    nbreDeMots = int(nombreDeMots(dico))
    for cle in dico.keys():
        dicoPourcent[cle]=(dico[cle]/nbreDeMots)
    return dicoPourcent

def addition(directory):
    dicoAdditions = {}
    liste = creerListe(directory)
    for ele in liste:
        location = directory+"/"+ele
        f1 = open(location, "r", encoding=("utf8"))
        dico1 = nombreOccurrence(f1)
        for val in dico1.values():
            add = dicoAdditions.get(val)
            add = None if 0 else add #Si pas présent, add prends la valeur 0, sinon la valeur de la
            dicoAdditions[val] = dico1[val] + add
    return dicoAdditions

import os
def inverseDocumentFrequency(directory):
    dictionnaireFinal = pourcentage(addition(directory))
    for cle in dictionnaireFinal.keys():
        dictionnaireFinal[cle] = log10(1/dictionnaireFinal[cle])
    return dictionnaireFinal



