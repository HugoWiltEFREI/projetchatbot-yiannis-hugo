from fonctionsTFIDF import termFrequency, getCleanedFilesNames
import matplotlib.pyplot as plt


def plot(directory: str, val: int):
    dico2 = {}
    filesList = getCleanedFilesNames(directory)
    for file in filesList:
        with open("{}/{}".format(directory, file), 'r', encoding="utf8") as discours:
            dico = termFrequency(discours.read())
            for k, v in dico.items():
                if v > val:
                    dico2[k] = v
            lists = sorted(dico2.items())

            x, y = zip(*lists)
            plt.plot(x, y)
            plt.show()
