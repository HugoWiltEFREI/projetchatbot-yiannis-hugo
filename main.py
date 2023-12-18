from fonctionsDeBase import extractNomsPres, associationTxtPrenomPres, list_of_files
from fonctionsCleanedFolder import createCleanedFolder
from fonctionsSecondaires import *
from fonctionsEnPlus import plot
from fonctionsTokens import *
from fonctionsSimilarity import bestDocument, rechercheFirstOccurence, politesse
from fonctionsBonus import remove_accent

def mainMenu():
    while True:
        if __name__ == '__main__':
            print("————————————————————————Partie I ou Chatbot?————————————————————————")
            partie = str(input()).lower()
        if partie == "partie i":
            partIMenu()

        elif partie == "chatbot":
            chatbox()

def partIMenu():
    print("——————————————————————————————Partie I——————————————————————————————")
    fct = str(input("Quelle fonction voulez-vous utiliser? : ")).lower()

    # Fonction qui sert à extraire le Nom d'un Président grâce au nom du document
    if fct == "extractnomspres" or fct == "extraction":
        print("Quel nom de fichier voulez vous extraire : ")  # On demande de quel document on veux connaitre le Président
        fichier = str(input())  # On stock le nom du document de la variable nom
        print(extractNomsPres(fichier))  # On éxécute la fonction avec la variable nom et on imprime

    elif fct == "associationtxtprenompres" or fct == "association":
        print("Quel est le nom du Président : ")
        nom = str(input())
        print(associationTxtPrenomPres(nom))

    elif fct == "list_of_files" or fct == "liste":
        extension = str(input("extension : "))
        print(list_of_files("speeches", extension))

    elif fct == "createcleanedfolder" or fct == "nettoyage":
        createCleanedFolder()

    elif fct == "termfrequency" or fct == "tf":
        directory = str(input("Enter a text : "))
        print(termFrequency(directory))

    elif fct == "dicoidf" or fct == "idf":
        directory = str(input("Enter directory : "))
        print(dicoIDF(directory))

    elif fct == "tfidf":
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

    # Plot un graph qui montre le nombre d'occurrence de chaque mots > à val pour chaque documents du directory
    elif fct == "plot":
        directory = str(input("Enter directory : "))
        val = int(input("Enter a value above 20 : "))
        plot(directory, val)

    else:
        print("Fonction inconnue, README.txt pour plus d'informations.")

def chatbox():
    print("——————————————————————————————Chatbot!——————————————————————————————")
    fct = str(input("Quelle fonction voulez-vous utiliser? : ")).lower()

    if fct == "vecteurtfidd":
        question = str(input("Entrez la question : "))
        directory = str(input("Enter directory : "))
        print(vectorTFIDFQuestion(question, directory))

    elif fct == "tokenlist":
        question = str(input("Entrez votre question : "))
        print(tokenList(question))

    elif fct == "recherchecorpus":
        directory = str(input("Enter directory : "))
        question = str(input("Entrez votre question : "))
        print(rechercheCorpus(question, directory))

    elif fct == "scoretf":
        mot = str(input("Entrez un mot : "))
        question = str(input("Entrez votre question : "))
        print(scoreTF(mot, question))

    elif fct == "vectortfidfquestion":
        directory = str(input("Enter directory : "))
        question = str(input("Entrez votre question : "))
        print(vectorTFIDFQuestion(question, directory))

    elif fct == "bestdocument":
        directory = str(input("Enter directory : "))
        question = str(input("Entrez votre question : "))
        vectorQuestion = vectorTFIDFQuestion(question, directory)
        matriceCorpus = matriceTFIDF(directory)
        print("Le document le plus similaire est :", bestDocument(vectorQuestion, matriceCorpus))

    elif fct == "recherchefirstoccurence":
        mot = str(input("Entrez un mot : "))
        file = str(input("Entrez un nom de fichier de speeches : "))
        print(rechercheFirstOccurence(mot, file))

    elif fct == "chatbot":
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

    elif fct == "bonus":
        print("⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕Bonus!⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕")
        fct = str(input("Quelle fonction voulez-vous utiliser? : ")).lower()

        if fct == "removeaccent":
            chaineDeC = str(input("Entrez une chaine de caractère : "))
            print(remove_accent(chaineDeC))

        elif fct == "textesbonus":
            directory = str(input("Enter directory : "))
            listeDiscours = getCleanedFilesNames(directory)
            
    elif fct == "help":
        with open("README.txt", "r", encoding="utf8") as f:
            for ligne in f:
                print(ligne)
    else:
        print("Fonction inconnue, README.txt pour plus d'informations.")

#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
        #lancement du programme

mainMenu()
