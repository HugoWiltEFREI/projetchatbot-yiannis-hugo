from math import log10
dico = {}
dicoPourcent = {}
dicoAdditions = {}


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

def pourcentage(texte):
    dictionnaireOccurrence = nombreOccurrence(texte)
    nbreDeMots = int(nombreDeMots(dictionnaireOccurrence))
    for cle in dictionnaireOccurrence.keys():
        dicoPourcent[cle]=(dictionnaireOccurrence[cle]/nbreDeMots)
    return dicoPourcent

def addition(directory):
    for filename in os.listdir(directory):


import os
def inverseDocumentFrequency(directory):
    for filename in os.listdir(directory):
