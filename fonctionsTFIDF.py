from math import log10
dico = {}
dicoPourcent = {}
dicoAdditions = {}
from fonctions import creerListe


def nombreOccurrence(chaineDeC):
    nombreOcc = dict()
    listeDeMots = chaineDeC.split()
    for mots in listeDeMots:
        if mots in nombreOcc:
            nombreOcc[mots] += 1
        else:
            nombreOcc[mots] = 1
    return nombreOcc

def nombreDeMots(dictionnaire):
    total = 0
    for i in dictionnaire.values():
        total += int(i)
    return total

def pourcentage(dico): #A changer pour effectuer calcul sur dico et pas texte
    nbreDeMots = int(nombreDeMots(dico))
    for cle in dico.keys():
        dicoPourcent[cle]=(dico[cle]/nbreDeMots)
    return dicoPourcent

def addition(directory):
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
    for filename in os.listdir(directory):
        print("r")
