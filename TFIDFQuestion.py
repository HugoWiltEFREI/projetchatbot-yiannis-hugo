from fonctionsTFIDF import dicoIDF, matriceTFIDF
from inputProcessing import tokenList

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
