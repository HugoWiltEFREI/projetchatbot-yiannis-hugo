from fonctionsTFIDF import dicoIDF, matriceTFIDF
from fonctionsCleanedFolder import identifySpeChr


def tokenList(chaineDeCToken: str):
    for c in chaineDeCToken:
        if identifySpeChr(c):
            chaineDeCToken = chaineDeCToken.replace(c, " ")
    for _ in chaineDeCToken:
        chaineDeCToken = chaineDeCToken.lower()
    questionToken = chaineDeCToken.split()
    if len(questionToken)!= 0:
        return questionToken
    else:
        return "Pas dans le corpus"


def rechercheCorpus(chaineDeCRecherche: str, directory: str):
    valPresente = set()
    for ele in tokenList(chaineDeCRecherche):
        if (ele in dicoIDF(directory)) and (ele not in valPresente):
            valPresente.add(ele)
    return valPresente


def scoreTF(mot: str, question: str):
    score = 0
    listeTokens = tokenList(question)
    for token in listeTokens:
        if token == mot:
            score += 1
    return score


def vectorTFIDFQuestion(question: str, directory: str):
    matrice = matriceTFIDF(directory)
    IDF = dicoIDF(directory)
    dicoVectorTFIDFQuestion = {}
    for discours in matrice.keys():
        for mot in matrice[discours].keys():
            if mot not in dicoVectorTFIDFQuestion.keys():
                dicoVectorTFIDFQuestion[mot] = scoreTF(mot, question) * IDF[mot]
    return dicoVectorTFIDFQuestion
