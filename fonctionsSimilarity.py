from math import sqrt 
def produitScalaire(vecteurA, vecteurB):
    produit = float(0)
    for mot in vecteurA.keys():
        if mot in vecteurB.keys():
            produit+=vecteurA[mot]*vecteurB[mot]
    return produit

def normeVector(vector):
    norme=0
    for mot in vector.keys():
        norme+=vector[mot]**2
    norme=sqrt(norme)
    if norme!=0:
        return norme
    else:
        return 1

def similarityScore(vectorA,vectorB):
    score=produitScalaire(vectorA,vectorB)/(normeVector(vectorA)*normeVector(vectorB))
    return score

def bestDocument(vectorQuestion,matriceCorpus):
    meilleurs={"nom":"Aucun discours ne correspond à cette question.","score":0}
    scoreDoc=0
    for document in matriceCorpus.keys():
        scoreDoc=similarityScore(vectorQuestion,matriceCorpus[document])
        if scoreDoc>meilleurs["score"]:
            meilleurs["nom"]=document
            meilleurs["score"]=scoreDoc
    return meilleurs["nom"]


import TFIDFQuestion,fonctionsTFIDF
while True :
    print(bestDocument(TFIDFQuestion.vectorTFIDFQuestion(input("Saisir la question : "),"cleaned"),fonctionsTFIDF.matriceTFIDF("cleaned")))