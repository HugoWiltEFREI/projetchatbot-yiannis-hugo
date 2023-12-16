from math import sqrt 
def produitScalaire(vecteurA, vecteurB):
    produit = float(0)
    for mot in vecteurA.keys():
        produit+=vecteurA[mot]*vecteurB[mot]
    return produit

def normeVector(vector):
    norme=0
    for mot in vector.keys():
        norme+=vector[mot]**2
    norme=sqrt(norme)
    return norme

def similarityScore(vectorA,vectorB):
    score=produitScalaire(vectorA,vectorB)/(normeVector(vectorA)*normeVector(vectorB))

def bestDocument(vectorQuestion,matriceCorpus):
    meilleurs={"nom":None,"score":0}
    scoreDoc=0
    for document in matriceCorpus.keys():
        scoreDoc=similarityScore(vectorQuestion,matriceCorpus[document])
        if scoreDoc>meilleurs[score]:
            meilleurs["nom"]=document
            meilleurs["score"]=scoreDoc
    return meilleurs["nom"]

