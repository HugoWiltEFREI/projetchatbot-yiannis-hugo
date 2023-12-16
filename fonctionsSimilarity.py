def produitScalaire(vecteurA, vecteurB):
    produit = float(0)
    for discours in vecteurA.keys():
        for mot in vecteurA[discours].keys():
            produit+=vecteurA[discours][mot]*vecteurB[discours][mot]
    return produit

import fonctionsTFIDF, TFIDFQuestion

vectorQ=TFIDFQuestion.matriceTFIDFQuestion("Salut, je voudrais savoir qui est Yiannis Leblanc !","cleaned")
print(produitScalaire(fonctionsTFIDF.matriceTFIDF("cleaned"),vectorQ))