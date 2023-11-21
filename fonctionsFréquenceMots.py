import os
#La fonction remplie dans vectors le dictionnaire d'occurrence de chaque mot du fichier file
def createVector(file,vectors,directory):
    nom=file[8:-4]
    vectors[nom]={}
    with open("{}/{}".format(directory,file),'r',encoding="utf8") as file:
        for mot in file.readlines():
            if mot[:-1] in vectors[nom].keys():
                vectors[nom][mot[:-1]]+=1
            else:
                vectors[nom][mot[:-1]]=1
#La fonction renvoie un tuple des noms de chaque fichier du dossier directory       
def getCleanedFilesNames(directory):
    list=[]
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            list.append(file)
    return tuple(list)
#La fonction renvoie les vecteur sous forme de dicos
#Dico sous forme : [nom président + numéro] -> Mot -> nbOccurrence
def getVectorsDico(directory):
    vectors={}
    filesList=getCleanedFilesNames(directory)
    for file in filesList:
        createVector(file,vectors,directory)
    return vectors
#Renvoie dictionnaire de l'ensemble des mots et leurs occurrences tout fichier confondu
# Mot -> Occurence
def getWordsOccurrenceDico(directory):
    occur={}
    vectors=getVectorsDico(directory)
    for discours in vectors.keys():
        for mot in vectors[discours].keys():
            if mot in occur:
                occur[mot]+=vectors[discours][mot]
            else:
                occur[mot]=vectors[discours][mot]
    return occur



