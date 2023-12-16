from fonctionsDeBase import *
from fonctionsTFIDF import *
from fonctionsCleanedFolder import *
from fonctionsSecondaires import *
from fonctionsEnPlus import plot

if __name__ == '__main__':
    fct = str(input("Quelle fonction voulez-vous utiliser? : "))

    # Fonction qui sert à extraire le Nom d'un Président grâce au nom du document
    if fct == "extractNomsPres" or fct == "extraction":
        print("Quel nom de fichier voulez vous extraire")  # On demande de quel document on veux connaitre le Président
        fichier = str(input())  # On stock le nom du document de la variable nom
        print(extractNomsPres(fichier))  # On éxécute la fonction avec la variable nom et on imprime

    elif fct == "associationTxtPrenomPres" or fct == "association":
        print("Quel est le nom du Président : ")
        nom = str(input())
        print(associationTxtPrenomPres(nom))

    elif fct == "list_of_files" or fct == "liste":
        extension = str(input("extension : "))
        print(list_of_files("speeches", extension))

    elif fct == "createCleanedFolder" or fct == "nettoyage":
        createCleanedFolder()

    elif fct == "termFrequency" or fct == "TF":
        directory = str(input("Enter a text : "))
        print(termFrequency(directory))

    elif fct == "dicoIDF" or fct == "IDF":
        directory = str(input("Enter directory : "))
        print(dicoIDF(directory))

    elif fct == "TF-IDF":
        directory = str(input("Enter directory : "))
        print(matriceTFIDF(directory))

    # Fait les questions de (Fonctionnalités à développer)
    elif fct == "programmes":
        print("La liste des mots avec un score TF-IDF de 0 est : ", uselessWordsList("cleaned"))
        val = float(input("Entrez la rareté que vous voulez (0-1):"))
        print("La liste des mots avec un score TF-IDF de ", val, "est :", rareWordsList("cleaned", val))
        print("Mot le + utilisé par Chirac est :", motImportantDiscours(additionDico(["Chirac1.txt", "Chirac2.txt"], "cleaned")))
        print("Mot prononcé par :", motDit("nation", "cleaned"))
        print("Premier président à dire climat est", firstOccurrence("climat", "cleaned"))
        print("Premier président à dire écologie est", firstOccurrence("écologie", "cleaned"))
        print("Mots que tous les présidents ont évoques (hormis non important", recurrentWordsList("cleaned"))

    elif fct == "help":
        with open("README.txt", "r", encoding="utf8") as f:
            for ligne in f:
                print(ligne)

    # Plot un graph qui montre le nombre d'occurrence de chaque mots > à val pour chaque documents du directory
    elif fct == "plot":
        directory = str(input("Enter directory: "))
        val = int(input("Enter a value above 20: "))
        plot(directory, val)

    else:
        print("Fonction inconnue, README.txt pour plus d'informations.")
        
