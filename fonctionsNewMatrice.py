from fonctionsTFIDF import getCleanedFilesNames, termFrequency, matriceTFIDF
def tailleMatrice(directory):
    somme = 0
    dico = {}
    dico2 = {}
    filesList = getCleanedFilesNames(directory)
    for discours in filesList:
        with open("{}/{}".format(directory, discours), 'r', encoding="utf8") as file:
            dico[discours] = termFrequency(file.readline())
        for values1 in dico.values():
            for keys, values2 in values1.items():
                if keys not in dico2:
                    dico2[keys] = 1
    return sum(dico2[item] for item in dico2)


def creationMatrice(directory):
    L = []
    nbLig = len(getCleanedFilesNames(directory))+1
    nbCol = tailleMatrice(directory)
    for i in range(nbCol):
        L.append([0.0]*nbLig)
    return L

def matriceDicoToMatriceList(matrice,directory):
    liste = creationMatrice(directory)
    matriceA = matriceTFIDF(directory)
    i = 0
    j = 0
    k = 0
    for val in matrice.values():
        i+=1
        for keys, values in val.items():
            if liste[j][0] != 0 and isInList(keys,liste)==False:
                j+=1
            elif liste[j][0] == 0 and isInList(keys,liste)==False:
                liste[j][0] = keys
                liste[j][i] = round(values,3)
                if j<(len(liste)-1):
                    j+=1
            elif isInList(keys,liste)==True:
                while liste[k][0] != keys and k<(len(liste)-1):
                    k = k+1
                liste[k][i] = round(values,3)
            k = 0
    return liste

def isInList(element,liste):
    for i in range(len(liste)):
        if liste[i][0] == element:
            return True
    else:
        return False



