import os
from math import log10


def termFrequency(chaineDeC: str):  # On définie la fct nombreOccurrence avec comme argument chaine de caractère
    for i in "./,?!:":
        chaineDeC = chaineDeC.replace(i, "")
    nombreOcc = dict()  # On créer un dico vide où l'on va stocker le nombre d'occurrence des mots dans la chaine
    listeDeMots = chaineDeC.split()  # On délimite les mots en regardant où sont les espaces et on les stocks dans un liste
    for mots in listeDeMots:
        if mots in nombreOcc:
            nombreOcc[mots] += 1  # Si le mot est déjà dans le dico, on fait +1
        else:
            nombreOcc[mots] = 1  # Sinon on rajoute le mot dans le dico avec la valeur 1
    return nombreOcc


# La fonction renvoie un tuple des noms de chaque fichier du dossier directory
def getCleanedFilesNames(directory: str):
    listeCleaned = []
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            listeCleaned.append(file)
    return tuple(listeCleaned)


def dicoIDF(directory: str):
    dicoMots = {}
    nbFichier = 0
    filesList = getCleanedFilesNames(directory)
    for discours in filesList:
        nbFichier += 1
        with open("{}/{}".format(directory, discours), 'r', encoding="utf8") as file:
            setMots = set()
            for mot in file.read().split():
                if not (mot in setMots):
                    setMots.add(mot)
                    if mot in dicoMots.keys():
                        dicoMots[mot] += 1
                    else:
                        dicoMots[mot] = 1
    for mot in dicoMots.keys():
        dicoMots[mot] = log10(nbFichier / dicoMots[mot])
    return dicoMots


def matriceTFIDF(directory: str):
    TFIDF = {}
    filesList = getCleanedFilesNames(directory)
    IDF = dicoIDF(directory)
    for file in filesList:
        with open("{}/{}".format(directory, file), 'r', encoding="utf8") as discours:
            TF = termFrequency(discours.read())
        TFIDF[file[:-4]] = {}
        for mot in TF:
            TFIDF[file[:-4]][mot] = TF[mot] * IDF[mot]
    return TFIDF
