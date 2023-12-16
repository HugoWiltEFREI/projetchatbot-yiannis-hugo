from fonctionsTFIDF import dicoIDF, matriceTFIDF
from fonctionsCleanedFolder import identifySpeChr
def tokenList(chaineDeCToken:str):
    for c in chaineDeCToken:
        if identifySpeChr(c):
            chaineDeCToken = chaineDeCToken.replace(c, " ")
    for i in chaineDeCToken:
        chaineDeCToken = chaineDeCToken.lower()
    questionToken = chaineDeCToken.split()
    return questionToken

def rechercheCorpus(chaineDeCRecherche:str, directory):
    valPresente = set()
    for ele in tokenList(chaineDeCRecherche):
        if (ele in dicoIDF(directory)) and (ele not in valPresente):
            valPresente.add(ele)
    return valPresente

def scoreTF(mot,question):
    score=0
    listeTokens=tokenList(question)
    for token in listeTokens:
        if token==mot:
            score+=1
    return score

def vectorTFIDFQuestion(question,corpusDirectory):
    matrice=matriceTFIDF(corpusDirectory)
    IDF=dicoIDF(corpusDirectory)
    vectorTFIDFQuestion={}
    for discours in matrice.keys():
        for mot in matrice[discours].keys():
            if not mot in vectorTFIDFQuestion.keys():
                vectorTFIDFQuestion[mot]=scoreTF(mot,question)*IDF[mot]
    return vectorTFIDFQuestion


