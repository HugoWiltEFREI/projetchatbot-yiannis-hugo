from fonctions import *

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
        e


    elif fct == "list_of_files":
        directory = str(input("directory : "))
        extension = str(input("extension : "))
        print(list_of_files(directory, extension))

    elif fct == "createCleanedFolder" or fct == "nettoyage":
        createCleanedFolder()

    else:
        print("Fonction inconnue, README.txt pour plus d'informations.")
