from fonctionsTFIDF import dicoIDF, matriceTFIDF

def scoreTF(mot,question):
    score=0
    listeTokens=tokenList(question)
    for token in listeTokens:
        if token==mot:
            score+=1
    score=score/len(listeTokens)
    return score

def TFIDFQuestion(question,corpusDirectory):
    matrice=matriceTFIDF(corpusDirectory)
    IDF=dicoIDF(corpusDirectory)
    for discours in matrice.keys():
        for mot in matrice[discours].keys():
            matrice[discours][mot]=scoreTF(mot,question)*IDF[mot]
    return matrice
