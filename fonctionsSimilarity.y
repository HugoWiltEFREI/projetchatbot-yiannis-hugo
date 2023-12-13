from math import sqrt
from fonctionsNewMatrice import *
from fonctionsTokens import vecteurTFIDF
def produitScalaire(vecteurA, vecteurB):
    M = len(vecteurA)
    produit = float(0)
    for i in range(M):
        produit += vecteurA[i]*vecteurB[i]
    return produit

def normeVecteur(vecteur):
    M = len(vecteur)
    norme = float(0)
    for i in range(M):
        norme += vecteur[i]*vecteur[i]
    return sqrt(norme)

def similarity(vecteurA,vecteurB):
    return (produitScalaire(vecteurA,vecteurB))/(normeVecteur(vecteurA)*normeVecteur(vecteurB))

def docPlusPertinent(matriceTFIDF,vecteurTFIDF):
    maxSim = 0
    sim = 0
    k = 0
    for i in range(len(matriceTFIDF[0])-1):
        for j in range(len(matriceTFIDF)):
            for keys, values in vecteurTFIDF.items():
                if values != 0.0:
                    while matriceTFIDF[k][0] != keys:
                        k = k + 1
                    sim += similarity(keys, matriceTFIDF[j][i+1])
        if maxSim<sim:
            maxSim = sim
    return maxSim


def equivalentNom(nomFichier):
    return "Nomination_"+nomFichier

matrice = matriceDicoToMatriceList(matriceTFIDF("cleaned"),"cleaned")
print(docPlusPertinent(matrice,vecteurTFIDF("Peux-tu me dire comment une nation peut-elle prendre soin du climat","cleaned")))
