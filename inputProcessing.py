# Il est impossible de modifier la fct "createTokenFile()" pour cette étape, le fctmnt est trop différent
from fonctionsCleanedFolder import identifySpeChr
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
