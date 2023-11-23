
def nombreOccurrence(chaineDeC): #On définie la fct nombreOccurrence avec comme argument chaine de caractère
    nombreOcc = dict()  #On créer un dico vide où l'on va stocker le nombre d'occurrence des mots dans la chaine
    listeDeMots = chaineDeC.split() #On délimite les mots en regardant où sont les espaces et on les stocks dans un liste
    for mots in listeDeMots:
        if mots in nombreOcc:
            nombreOcc[mots] += 1 #Si le mot est déjà dans le dico, on fait +1
        else:
            nombreOcc[mots] = 1 #Sinon on rajoute le mot dans le dico avec la valeur 1
    return nombreOcc



