from math import sqrt
from fonctionsTokens import vectorTFIDFQuestion
from fonctionsTFIDF import matriceTFIDF


def produitScalaire(vecteurA: dict, vecteurB: dict):
    produit = float(0)
    for mot in vecteurA.keys():
        if mot in vecteurB.keys():
            produit += vecteurA[mot] * vecteurB[mot]
    return produit


def normeVector(vector: dict):
    norme = 0
    for mot in vector.keys():
        norme += vector[mot] ** 2
    norme = sqrt(norme)
    if norme != 0:
        return norme
    else:
        return 1


def similarityScore(vectorA: dict, vectorB: dict):
    score = produitScalaire(vectorA, vectorB) / (normeVector(vectorA) * normeVector(vectorB))
    return score


def equivalentNom(nomFichier: str):
    return "Nomination_" + nomFichier + ".txt"


def bestDocument(vectorQuestion: dict, matriceCorpus: dict):
    meilleurs = {"nom": "Aucun discours ne correspond à cette question.", "score": 0}
    for document in matriceCorpus.keys():
        scoreDoc = similarityScore(vectorQuestion, matriceCorpus[document])
        if scoreDoc > meilleurs["score"]:
            meilleurs["nom"] = document
            meilleurs["score"] = scoreDoc
    return equivalentNom(meilleurs["nom"])


def motScoreTFIDF(question: str, directory: str):
    return max(vectorTFIDFQuestion(question, directory), key=vectorTFIDFQuestion(question, directory).get)


def rechercheFirstOccurence(mot: str, document: str):
    motMin = mot.lower()
    with open("speeches/{}".format(document), "r", encoding="utf8") as f1:
        liste = f1.read().lower().split("\n")
        for i in range(len(liste)):
            val = liste[i].find(motMin)
            if val != -1:
                return liste[i]


def politesse(question: str, directory: str):
    question_starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr!"
    }
    document = bestDocument(vectorTFIDFQuestion(question, directory), matriceTFIDF(directory))
    reponseQuestion = rechercheFirstOccurence("climat", document)
    debutDePhrase = question.split()[0]
    for keys, values in question_starters.items():
        if str(keys) == debutDePhrase:
            if str(keys) == "Peux-tu":
                return values + " " + reponseQuestion.capitalize()
            else:
                return values + " " + reponseQuestion
