from fonctionsTFIDF import termFrequency, getCleanedFilesNames, matriceTFIDF
from fonctionsBonus import remove_accent

def additionDico(listeDico, directory):
    dicoAdd = {}
    for dico in listeDico:
        with open("{}/{}".format(directory, dico), 'r', encoding="utf8") as file1:
            chaine = file1.read()
            dictionnaire = termFrequency(chaine)
        dicoAdd.update(dictionnaire)
        file1.close()
    return dicoAdd

def motDit(mot,
           directory):  # Retourne un dico avec le nombre d'occurrence du mot si le mot et dit avec le nom du discours en clé et le nombre d'occurrence en valeur
    dico = {}  # retourne aussi le doc où le mot est dit le + de fois
    for discours in getCleanedFilesNames(directory):
        with open("{}/{}".format(directory, discours), 'r', encoding="utf8") as file1:
            chaine = file1.read()
            dictionnaire = termFrequency(chaine)
            if mot in dictionnaire.keys():
                dico[discours] = dictionnaire[mot]
        motMax = max(dico, key=dico.get)
        file1.close()
    return dico, motMax[:-4]


def firstOccurrence(motCherche, directoryOccurrence):
    dicoOccurrence = {}  # retourne aussi le doc où le mot est dit le + de fois
    for discoursOccurrence in getCleanedFilesNames(directoryOccurrence):
        with open("{}/{}".format(directoryOccurrence, discoursOccurrence), 'r', encoding="utf8") as file1:
            listeMot = file1.read().split()
            for i in range(len(listeMot)):
                if str(listeMot[i]) == motCherche:
                    dicoOccurrence[discoursOccurrence] = i + 1
                    break
            file1.close()
    if dicoOccurrence == {}:
        return "personne"
    else:
        valMin = min(dicoOccurrence, key=dicoOccurrence.get)
        return valMin[:-4]


def uselessWordsList(directory):
    matrice = matriceTFIDF(directory)
    useless = set()
    for discours in matrice.keys():
        for mot in matrice[discours].keys():
            if matrice[discours][mot] == 0:
                useless.add(mot)
    return useless


def rareWordsList(directory, val):
    matrice = matriceTFIDF(directory)
    rare = set()
    for discours in matrice.keys():
        for mot in matrice[discours].keys():
            if matrice[discours][mot] >= val:
                rare.add(mot)
    return rare


def recurrentWordsList(directory):
    scoreMinimum = 2
    uselessWords = uselessWordsList(directory)
    recurrentWords = set()
    for file in getCleanedFilesNames(directory):
        with open("{}/{}".format(directory, file), 'r', encoding="utf-8") as discours:
            dicoTF = termFrequency(discours.read())
            for mot in dicoTF.keys():
                if dicoTF[mot] < scoreMinimum and mot in uselessWords:
                    recurrentWords.add(mot)
        discours.close()
    return recurrentWords

def motImportantDiscours(dico,directory):
    valMax= -100
    mot = ""
    for cle, val in dico.items():
        if remove_accent(cle) not in uselessWordsList(directory):
            if val>valMax:
                valMax = val
                mot = cle
    return mot
