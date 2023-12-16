from unidecode import unidecode
import os

def remove_accent(chaineDeC):
    return unidecode(chaineDeC)

feminin = ["elevation","ecole","energie","innovation","election","expression","alternance","organisation","union","histoire","audace","action","economie","independance","imminence","ere","ecoute","attente","aprete","efficacite","ouverture","economie","emotion","innovation","exigence","impatience","arene","universalite","education","etroitesse","obligation","adresse","identite","afrique","egalite","emancipation","initiative","intolerance","excellence","exemplarite","instabilite","imagination","instabilite","election","unite","action","etroitesse","issue","aide","idee","universalite","oree","aube","idee","aide","irruption","europe","exclusion","aspiration","autorite"]
masculin = ["indispensable","attachement","antisemitisme","imperatif","hotel","horizon","ensemble","ordre","effort","esprit","executif","elan","accord","exercice","accomplissement","emploi","an","avenir","immobilisme","hexagone","accompagnement","abaissement","absolutisme","investissement","amour", "honneur","exemple","affrontement","etranger","etat","executif","accomplissement","emploi","horizon","exterieur","esprit","instrument","extremisme","homme","effort","espoir","emploi","interet","evenement","ideal"]
autre = ["avait","affirme","assumerai","autre","a","avez","accorder","immense","aborde","on","ont","ete","issue","attendent","elevation","emporter"]

def lelales(chaineDeC):
    chaineDeC = remove_accent(chaineDeC)
    if chaineDeC[:2]=="l'":
        if chaineDeC[2:] in feminin:
                chaineDeC = "la "+chaineDeC[2:]

        elif chaineDeC[2:] in masculin:
            chaineDeC = "le "+chaineDeC[2:]
        else:
             chaineDeC ="la "+chaineDeC[2:]
    return chaineDeC

def que(chaineDeC):
    if chaineDeC[:3]=="qu'":
        chaineDeC ="que "+chaineDeC[3:]
    return chaineDeC

def textesBonus(listeDiscours):
    for ele in listeDiscours:
        with open("speeches/{}".format(ele), "r", encoding="utf8") as f1, open(
                "cleaned2/{}".format("Bonus_"+ele[11:]), "w", encoding="utf8") as f2:
            liste = f1.read().lower().split()
            for i in range(len(liste)):
                liste[i] = remove_accent(liste[i])
                liste[i] = que(liste[i])
                liste[i] = lelales(liste[i])
                f2.write(liste[i]+" ")
    return liste

listenom = ['Nomination_Chirac1.txt', 'Nomination_Chirac2.txt', 'Nomination_Giscard dEstaing.txt', 'Nomination_Hollande.txt', 'Nomination_Macron.txt', 'Nomination_Mitterrand1.txt', 'Nomination_Mitterrand2.txt', 'Nomination_Sarkozy.txt']

textesBonus(listenom)



