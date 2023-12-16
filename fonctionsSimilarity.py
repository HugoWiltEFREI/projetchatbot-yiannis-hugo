def lenVector(vector):
    

def produitScalaire(vecteurA, vecteurB):
    M = len(vecteurA)
    produit = float(0)
    for i in range(M):
        produit += vecteurA[i]*vecteurB[i]
    return produit