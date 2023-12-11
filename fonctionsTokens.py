from fonctionsTFIDF import *
def tokenQuestion(chaineDeCToken:str):
    for i in ",?;.:/!":
        chaineDeCToken = chaineDeCToken.replace(i, " ")
    for i in chaineDeCToken:
        chaineDeCToken = chaineDeCToken.lower()
    questionToken = chaineDeCToken.split()
    return questionToken

def rechercheCorpus(chaineDeCRecherche:str, directory):
    valPresente = []
    for ele in tokenQuestion(chaineDeCRecherche):
        if (ele in dicoIDF(directory)) and (ele not in valPresente):
            valPresente.append(ele)
    return valPresente


def vecteurTF(question:str,directory):
    dicoVecteurTF = {}
    tokQue = tokenQuestion(question)
    long = len(tokQue)
    recherche = rechercheCorpus(question, directory)
    for mot in tokQue:
        if (mot in recherche) and (mot in dicoVecteurTF.keys()):
            dicoVecteurTF[mot] += 1 / long
        elif mot in recherche and mot not in dicoVecteurTF.keys():
            dicoVecteurTF[mot] = 1 / long
        else:
            dicoVecteurTF[mot] = 0
    return dicoVecteurTF
def vecteurTFIDF(question:str,directory):
    dicoVecteurTFIDF = {}
    matrice = matriceTFIDF(directory)
    for keys,values in vecteurTF(question,directory).items():
        for vals in matrice.values():
            for ke, va in vals.items():
                if keys == ke:
                    dicoVecteurTFIDF[keys] = values*va
    return dicoVecteurTFIDF

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
print(tailleMatrice("cleaned"))

def matriceDicoToMatriceList(matrice):
    print("hello")
