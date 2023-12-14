from fonctionsTFIDF import dicoIDF, matriceTFIDF
from fonctionsCleanedFolder import identifySpeChr
def tokenQuestion(chaineDeCToken:str):
    for c in chaineDeCToken:
        if identifySpeChr(c):
            chaineDeCToken = chaineDeCToken.replace(c, " ")
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



