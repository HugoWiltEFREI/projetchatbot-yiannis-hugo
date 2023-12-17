from fonctionsDeBase import *
from fonctionsCleanedFolder import *
from fonctionsSecondaires import *
from fonctionsEnPlus import plot
from fonctionsTokens import *
from fonctionsSimilarity import *
from fonctionsBonus import *

if __name__ == '__main__':
    print("————————————————————————Partie I ou Chatbot?————————————————————————")
    partie = str(input())
    if partie == "Partie I":
        print("——————————————————————————————Partie I——————————————————————————————")
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
            val = float(input("Entrez la rareté que vous voulez :"))
            print("La liste des mots avec un score TF-IDF de ", val, "+ est :", rareWordsList("cleaned", val))
            print("Mot le + utilisé par Chirac est :", motImportantDiscours(additionDico(["Chirac1.txt", "Chirac2.txt"], "cleaned"), "cleaned"))
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
    elif partie == "Chatbot":
        print("——————————————————————————————Chatbot!——————————————————————————————")
        fct = str(input("Quelle fonction voulez-vous utiliser? : "))

        if fct == "vecteurTFIDF":
            question = str(input("Entrez la question"))
            directory = str(input("Enter directory : "))
            print(vectorTFIDFQuestion(question, directory))

        elif fct == "tokenList":
            question = str(input("Entrez votre question:"))
            print(tokenList(question))

        elif fct == "rechercheCorpus":
            directory = str(input("Enter directory : "))
            question = str(input("Entrez votre question:"))
            print(rechercheCorpus(question, directory))

        elif fct == "scoreTF":
            mot = str(input("Entrez un mot : "))
            question = str(input("Entrez votre question:"))
            print(scoreTF(mot, question))

        elif fct == "vectorTFIDFQuestion":
            directory = str(input("Enter directory : "))
            question = str(input("Entrez votre question:"))
            print(vectorTFIDFQuestion(question, directory))

        elif fct == "bestDocument":
            directory = str(input("Enter directory : "))
            question = str(input("Entrez votre question:"))
            vectorQuestion = vectorTFIDFQuestion(question, directory)
            matriceCorpus = matriceTFIDF(directory)
            print("Le document le plus similaire est :", bestDocument(vectorQuestion, matriceCorpus))

        elif fct == "rechercheFirstOccurence":
            mot = str(input("Entrez un mot : "))
            file = str(input("Entrez un nom de fichier de speeches"))
            print(rechercheFirstOccurence(mot, file))

        elif fct == "Chatbot":
            encore = True
            directory = str(input("Enter directory : "))
            while encore:
                question = str(input("Que puis-je faire pour vous? "))
                print(politesse(question, directory))
                encore = str(input("Avez vous encore une question? "))
                if encore == "Oui":
                    encore = True
                else:
                    encore = False

        elif fct == "Bonus":
            print("⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕Bonus!⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕")
            fct = str(input("Quelle fonction voulez-vous utiliser? : "))
            if fct == "removeAccent":
                chaineDeC = str(input("Entrez une chaine de caractère"))
                print(remove_accent(chaineDeC))

            elif fct == "textesBonus":
                directory = str(input("Enter directory : "))
                listeDiscours = getCleanedFilesNames(directory)

        else:
            print("Fonction inconnue, README.txt pour plus d'informations.")
