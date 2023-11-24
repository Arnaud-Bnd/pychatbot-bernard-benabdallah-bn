import os
import random
from math import *

def list_of_files(directory, extension):
    files_names = []        # créer une liste qui va contenir les noms des fichiers
    for filename in os.listdir(directory):
        if filename.endswith(extension):        # selection seulement les fichiers textes
            files_names.append(filename)        # ajoute les noms des fichiers textes à la liste files_names
    return files_names

# Call of the function

directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)


# Extraire nom président
def extract_name(liste):        # extrait seulement le nom de chaque président à partir du nom des fichiers textes
    for i in range(len(liste)):
        liste[i] = liste[i][11:-4]      # enlève le "Nomination_" et le ".txt"
        if '1' in liste[i] or '2' in liste[i]:
            liste[i] = liste[i][:-1]        # enlève le "1" et le "2" s'il y a plusieurs fichiers pour un même président
    return liste

# Call of the function
"""
extract_name(files_names)
print(files_names)
"""


# Associer prénom président
def name_pres():        # Créer un dictionnaire qui associe un prénom au nom du président
    prenom_nom = {'Chirac' : 'Jacques',
                  'Mitterrand' : 'François',
                  'Sarkozy' : 'Nicolas',
                  'Macron' : 'Emmanuel',
                  'Giscard dEstaing' : 'Valéry',
                  }
    return prenom_nom
"""    for i in range (len(liste)):
        if (liste[i] == 'Chirac'):
            liste[i] = 'Jacques Chirac'
        elif (liste[i] == 'Mitterrand'):
            liste[i] = 'François Mitterrand'
        elif (liste[i] == 'Sarkozy'):
            liste[i] = 'Nicolas Sarkozy'
        elif (liste[i] == 'Macron'):
            liste[i] = 'Emmanuel Macron'
        elif (liste[i] == 'Giscard dEstaing'):
            liste[i] = 'Valéry Giscard dEstaing'
        elif (liste[i] == 'Hollande'):
            liste[i] = 'François Hollande'
"""

# Call of the function
"""
print(name_pres())
"""


# Extraire nom président + numéro discours
def extract_name_file(liste):       # extrait le nom du président et le numéro s'il y en a un (sera utile pour parcours les fichiers)
    for i in range(len(liste)):
        liste[i] = liste[i][11:-4]
    return liste


# Mettre en minuscule
def minuscule(mot):     # met tous les caractères alphabétiques en minuscule
    nouveau_mot = ""        # créer une nouvelle chaîne de caractère pour conserver l'ancienne
    nouveau_mot = list(nouveau_mot)     # convertie la chaîne de caractère en liste
    mot = list(mot)     # convertie la chaîne de caractère en liste
    for i in range(len(mot)):
        if (ord('A') <= ord(mot[i])) and (ord(mot[i]) <= ord('Z')):     # sélectionne uniquement les caractères en majuscule
            mot[i] = chr(ord(mot[i]) + (ord('a') - ord('A')))       # convertion en minuscule
        nouveau_mot.append(mot[i])      # ajoute à la nouvelle chaîne de caractère
    return ''.join(nouveau_mot)     # reconvertie la liste en chaîne de caractère

#print(minuscule("OUI"))

def ponctuation(mot):
    nouveau_mot = ""        # créer une nouvelle chaîne de caractère pour conserver l'ancienne
    nouveau_mot = list(nouveau_mot)     # convertie la chaîne de caractère en liste
    mot = list(mot)     # convertie la chaîne de caractère en liste
    for i in range(len(mot)):
        #if (ord(mot[i]) == ord('!')) or (ord(mot[i]) == ord('"')) or (ord(mot[i]) == ord('.')) or (ord(mot[i]) == ord(':')) or (ord(mot[i]) == ord(';')) or (ord(mot[i]) == ord('?')): # sélectionne uniquement les caractères de ponctuation
        if ((ord(mot[i]) >= ord(':')) and (ord(mot[i]) <= ord('@'))) or ((ord(mot[i]) >= ord('!')) and (ord(mot[i]) <= ord('#'))) or ((ord(mot[i]) >= ord('(')) and (ord(mot[i]) <= ord('+'))) or (ord(mot[i]) == ord('.')) or (ord(mot[i]) == ord('/')) or ((ord(mot[i]) >= ord('[')) and (ord(mot[i]) <= ord('^'))) or ((ord(mot[i]) >= ord('{')) and (ord(mot[i]) <= ord('~'))):
            del mot[i]
        if (ord(mot[i]) == ord('-')) or (ord(mot[i]) == ord('_')) or (ord(mot[i]) == ord('—')) or (ord(mot[i]) == ord('–')):
            mot[i] = ' '
        if (ord(mot[i]) == ord("'")) or (ord(mot[i]) == ord("’")) or (ord(mot[i]) == ord('`')) or (ord(mot[i]) == ord('‘')):        # sélectionne uniquement les apostrophes et les tirets
            var = random.randint(1,2)
            if (mot[i-1] != ord('l')) or (var % 2 == 0):
                mot[i] = 'e '
            else:
                mot[i] = 'a '
        nouveau_mot.append(mot[i])      # ajoute à la nouvelle chaîne de caractère
    return ''.join(nouveau_mot)     # reconvertie la liste en chaîne de caractère

#for i in range (20):
#    print(ponctuation("l'exercice"))


def TF(chaine):
    dico = {}
    mot = ""

    for i in range(len(chaine)):
        if (chaine[i] != ' '):      # sélectionne tous les caractères jusqu'à un espace
            mot += chaine[i]        # ajoute les caractères sélectionnés à une chaine de caractère
        elif (chaine[i] == ' '):        # délimite le mot
            if mot not in dico:
                dico[mot] = 1       # si le mot n'est pas dans le dictionnaire, l'ajouter au dictionnaire assiocié à une valeur 1
            else:
                dico[mot] += 1      # sinon ajouter 1 à la valeur associée au mot
            mot = ""        # réinitialise la chaine de caractère

    if (len(mot) != 0):     # prise en compte du dernier mot
        if mot not in dico:
            dico[mot] = 1       # si le mot n'est pas dans le dictionnaire, l'ajouter au dictionnaire assiocié à une valeur 1
        else:
            dico[mot] += 1      # sinon ajouter 1 à la valeur associée au mot

    return dico


"""
chaine = "je suis accepter à efrei et je suis heureux"
dico = {}
mot = ""
for i in range(len(chaine)):
    if (chaine[i] != ' '):
        mot += chaine[i]
    elif (len(mot) != 0):
        dico[mot] = ""
        mot = ""
if (len(mot) != 0):
    dico[mot] = ""
print(dico)
"""



print(TF("je suis accepter à efrei et je suis heureux"))

def IDF(dico):
    n = len(files_names) # nombre de fichier
    for i in dico:
        dico[i] = log(n/dico[i])
    return dico


print(IDF(TF("je suis accepter à efrei et je suis heureux")))




extract_name_file(files_names)
for i in range(len(files_names)): # parcours tous les fichiers du répertoire /speeches
    name_minuscule = 'Nomination_' + str(files_names[i]) + '.txt'
    with open("./speeches/" + name_minuscule, 'r') as f1:
        corpus = f1.read()
    corpus = minuscule(corpus) # convertie le texte du fichier texte en minuscule
    with open ("./cleaned/Clean_" + name_minuscule, 'w') as f2:
        f2.write(corpus) # stocke le nouveau contenue en minuscule dans un répertoire /cleaned
        