# Il est impossible de modifier la fct "createTokenFile()" pour cette étape, le fctmnt est trop différent
from fonctionsCleanedFolder import identifySpeChr
import fonctionsTFIDF as TFIDF

def tokenList(text):
    tokens=[]
    index=-1
    inMot=False
    for car in text:
        if identifySpeChr(car):
            if inMot:
                inMot = False
        else:
            if not inMot:
                tokens.append("")
                index+=1
                inMot=True
            traiterLettreMinuscule(car, tokens, index)
    return tokens

def traiterLettreMinuscule(car, tokensList, index):
    if 'A' <= car <= 'Z':
        tokensList[index]+=(chr(ord(car) + ord('a') - ord('A')))
    elif 192 <= ord(car) <= 220:
        tokensList[index]+=(chr(ord(car) + ord('é') - ord('É')))
    elif car == 'Œ' or car == 'œ':
        tokensList[index]+=("oe")
    else:
        tokensList[index]+=(car)

def isInCorpus(mot):
    matrice=TFIDF.matrice("cleaned")
    corpus=set()
    inCorpus=False
    for discours in matrice.keys():
        if mot in matrice[discours].keys():
            inCorpus=True
    return inCorpus

#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#vector de question
from fonctionsTFIDF import dicoIDF

def scoreTF(mot,question):
    score=0
    listeTokens=tokenList(question)
    for token in listeTokens:
        if token==mot:
            score+=1
    score=score/len(listeTokens)
    return score

from fonctionsTFIDF import matriceTFIDF

def TFIDFQuestion(question,corpusDirectory):
    matrice=matriceTFIDF(corpusDirectory)
    IDF=dicoIDF(corpusDirectory)
    for discours in matrice.keys():
        for mot in matrice[discours].keys():
            matrice[discours][mot]=scoreTF(mot,question)*IDF[mot]
    return matrice

    
    

    

    
    
    

