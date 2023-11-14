import os

def identifySpeChr(car):
    if ((car>=' ' and car<='/')) or (car>=':' and car<='?') or (car>='[' and car<='`') or (car>='{' and car<='}') or car=='\n':
        return True
    else:
        return False
    
def createTokenFiles(nomDiscours):
    with open("speeches/{}".format(nomDiscours),"r",encoding=("utf8")) as f1, open("cleaned/cleaned_{}".format(nomDiscours[11:]),"w",encoding=("utf8")) as f2:
        inMot=False
        for car in f1.read():
            if identifySpeChr(car):
                if inMot==True:
                    f2.write('\n')
                    inMot=False
            else:
                if car>='A' and car<='Z':
                    f2.write(chr(ord(car)+ord('a')-ord('A')))
                    inMot=True
                elif ord(car)>=192 and ord(car)<=220:
                    f2.write(chr(ord(car)+ord('é')-ord('É')))
                else:
                    f2.write(car)
                    inMot=True
def createCleanedFolder():
    nomsDiscours=[]
    for nom in os.listdir("speeches"):
        if nom.endswith("txt"):
            nomsDiscours.append(nom)
    for nom in nomsDiscours:
        createTokenFiles(nom)

createCleanedFolder()
