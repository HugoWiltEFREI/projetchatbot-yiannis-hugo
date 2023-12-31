import os


# identifie un caractère spécial ou un retour à la ligne et renvoie True ou False
def identifySpeChr(car):
    if (' ' <= car <= '/') or (':' <= car <= '?') or ('[' <= car <= '`') or (
            '{' <= car <= '}') or car == '\n':
        return True
    else:
        return False


# pour 1 fichier discours la fonction crée son fichier de tokens dans le dossier cleaned
def createTokenFiles(nomDiscours : str):
    with open("speeches/{}".format(nomDiscours), "r", encoding="utf8") as f1, open(
            "cleaned/{}".format(nomDiscours[11:]), "w", encoding="utf8") as f2:
        inMot = False
        for car in f1.read():
            if identifySpeChr(car):
                if inMot:
                    f2.write(' ')
                    inMot = False
            else:
                inMot = traiterLettre(car, inMot, f2)


# créée pour diviser la fct createTokenFiles() en deux fonctions plus petites
def traiterLettre(car, inMot, f2):
    if 'A' <= car <= 'Z':
        f2.write(chr(ord(car) + ord('a') - ord('A')))
        inMot = True
    elif 192 <= ord(car) <= 220:
        f2.write(chr(ord(car) + ord('é') - ord('É')))
    elif car == 'Œ' or car == 'œ':
        f2.write("oe")
        inMot = True
    else:
        f2.write(car)
        inMot = True
    return inMot


# remplie le dossier cleaned avec les fichier tokens de chaque fichier du dossier speeches
def createCleanedFolder():
    nomsDiscours = []
    for nom in os.listdir("speeches"):
        if nom.endswith("txt"):
            nomsDiscours.append(nom)
    for nom in nomsDiscours:
        createTokenFiles(nom)


createCleanedFolder()
