import os
from math import log10

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
