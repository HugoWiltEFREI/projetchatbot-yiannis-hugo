from fonctionsDeBase import *
from fonctionsTFIDF import *
from fonctionsCleanedFolder import *
from fonctionsFréquenceMots import *
from fonctionsSecondaires import *


if __name__ == '__main__':
    fct = str(input("Quelle fonction voulez-vous utiliser? : "))

    if fct == "extractNomsPres" or fct == "extraction":  # Fonction qui sert à extraire le Nom d'un Président grâce au nom du document
        print("Quel nom de fichier voulez vous extraire")  # On demande de quel document on veux connaitre le Président
        fichier = str(input())  # On stock le nom du document de la variable nom
        extractNomsPres(2)
        print(extractNomsPres(fichier))  # On éxécute la fonction avec la variable nom et on imprime

    elif fct == "associationTxtPrenomPres" or fct == "association":
        print("Quel est le nom du Président : ")
        nom = str(input())
        print(associationTxtPrenomPres(nom))

    elif fct == "list_of_files":
        directory = str(input("directory : "))
        extension = str(input("extension : "))
        print(list_of_files(directory, extension))

    elif fct == "createCleanedFolder" or fct == "nettoyage":
        createCleanedFolder()

    elif fct == "TF":
        directory = str(input("Enter a text : "))
        print(termFrequency(directory))

    elif fct == "TF-IDF":
        directory = str(input("Enter directory : "))
        print(matriceTFIDF(directory))

    elif fct == "programmes": #Fait les questions de (Fonctionnalités à développer)
        print("La liste des mots avec un score TF-IDF de 0 est : ", end="")
        print(uselessWordsList("cleaned"))
        print("La liste des mots avec un score TF-IDF de val est : ", end="")
        print(rareWordsList("cleaned",0.9))
        print("Le mot le plus utilisé par Chirac est : ", end="")
        print(motImportantDiscours(additionDico(["Chirac1.txt", "Chirac2.txt"], "cleaned")))
        print(motDit("nation","cleaned"))
        print("Le mot est utilisé en premier par ", end="")
        print(firstOccurrence("climat", "cleaned"))
        print(firstOccurrence("écologie", "cleaned"))


    else:
        print("Fonction inconnue, README.txt pour plus d'informations.")
