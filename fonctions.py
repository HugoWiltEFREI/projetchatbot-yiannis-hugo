import os
def extractNomsPres(fichier):
    if type(fichier) != str:
        raise("Illegal type for vairable fichier. fichier must be a str.")
    for i in "0123456789":
        fichier = fichier.replace(i, "")  # On supprime les valeurs numériques
    return (fichier[11:-4])  # On effectue un slicing pour récupérer uniquement le nom

def associationTxtPrenomPres(nom):
    trouve = False  # Au début, on n'a pas trouvé le prénom, donc trouve = False
    ListeNomsPres = [["Chirac", "Jacques"], ["Giscard dEstaing", "Valéry"], ["Hollande", "François"],
                     ["Macron", "Emmanuel"], ["Mitterand", "François"],
                     ["Sarkozy", "Nicolas"]]  # On créé une liste qui associe le nom des présidents avec leurs prénoms
    for indice in range(len(ListeNomsPres)):  # On parcours la liste
        if ListeNomsPres[indice][
            0] == nom:  # On compare si le premier élément (indice 0) de chaques sous-tableaux est égal au nom
            print("Le prénom du Président", nom, "est",  ListeNomsPres[indice][1])  # Si oui, on affiche le prénom et le nom
            trouve = True
    if trouve == False:
        print("Inconnu au bataillon")  # Si non, on affiche que l'on n'a pas trouvé

def list_of_files(directory, extension):
    files_names = []  # On créé une liste vide
    for filename in os.listdir(directory):  # On parcours les documents dans le directory
        if filename.endswith(extension):
            files_names.append(
                filename)  # Si l'extension du document correspond avec celle demandée, on rajoute à la liste
    files_names2 = []  # On créé une nouvelle liste
    for indice2 in range(len(files_names)):
        if extractNomsPres(
                files_names[indice2]) not in files_names2:  # Si les nom n'est pas présent dans la liste, on le rajoute
            files_names2.append(extractNomsPres(files_names[indice2]))
    return files_names2
