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
Nombre_fichiers = len(files_names)


# Extraire nom président
def extract_name(liste):        # extrait seulement le nom de chaque président à partir du nom des fichiers textes
    for i in range(len(liste)):
        liste[i] = liste[i][11:-4]      # enlève le "Nomination_" et le ".txt"
        if '1' in liste[i] or '2' in liste[i]:
            liste[i] = liste[i][:-1]        # enlève le "1" et le "2" s'il y a plusieurs fichiers pour un même président
    return liste


# Associer prénom président
def name_pres():        # Créer un dictionnaire qui associe un prénom au nom du président
    prenom_nom = {'Chirac' : 'Jacques',
                  'Mitterrand' : 'François',
                  'Sarkozy' : 'Nicolas',
                  'Macron' : 'Emmanuel',
                  'Giscard dEstaing' : 'Valéry',
                  }
    return prenom_nom


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


def ponctuation(mot):
    sans_ponctuation = ""
    caracteres_permis = "aàâbcçdeéèêËfghiîïjklmnoôpqrstuùûüvwxyÿzAÀÂBCÇDEÉÈÊËFGHIÎÏJKLMNOÔPQRSTUÙÛÜVWXYŸZ0123456789 "
    #mot = list(mot)
    for caractere in mot:
        if caractere in caracteres_permis:
            sans_ponctuation += caractere
        elif (caractere == '-') or (caractere == '_') or (caractere == '—') or (caractere == '–'):      # sélectionne uniquement les tirets
            sans_ponctuation += ' '
        elif (caractere == "'") or (caractere == "’") or (caractere == '`') or (caractere == '‘'):        # sélectionne uniquement les apostrophes
            sans_ponctuation += 'e '
    return sans_ponctuation


def separation(chaine):
    l = []
    mot = ""
    for i in range(len(chaine)):
        if (chaine[i] != " "):      # sélectionne tous les caractères jusqu'à un espace
            mot += chaine[i]        # ajoute les caractères sélectionnés à une chaine de caractère
        elif (chaine[i] == " "):       # délimite le mot
            l.append(mot)       # si le mot n'est pas dans la chaine de caractère, l'ajouter à la liste
            mot = ""        # réinitialise la chaine de caractère
    if (len(mot) != 0):     # prise en compte du dernier mot
        l.append(mot)       # si le mot n'est pas dans la chaine de caractère, l'ajouter à la liste
    return l


def TF(liste):
    dico = {}
    for i in range(len(liste)):
        if liste[i] not in dico:
            dico[liste[i]] = 1       # si le mot n'est pas dans la chaine de caractère, l'ajouter au dictionnaire assiocié à une valeur 1
        else:
            dico[liste[i]] += 1      # sinon ajouter 1 à la valeur associée au mot
    return dico


def IDF(directory):
    dico = {}
    noms_fichiers = extract_name_file(files_names)
    for i in range(Nombre_fichiers):
        name_1 = "Clean_Nomination_" + str(noms_fichiers[i]) + ".txt"
        with open(directory + name_1, 'r') as f:        # ouverture du premier fichier texte
            contenue_1 = separation(f.read())
        occurence = TF(contenue_1)
        for j in range(Nombre_fichiers):
            if (j != i):        # évite de sélectionner le même fichier texte
                name_2 = "Clean_Nomination_" + str(noms_fichiers[j]) + ".txt"
                with open(directory + name_2, 'r') as f:        # ouverture d'un second fichier texte
                    contenue_2 = TF(separation(f.read()))
                count = 0
                for mot, t in occurence.items():
                    if mot in contenue_2:
                        count += 1
                    print(mot, count)
                    #dico[mot] = log((Nombre_fichiers / float(count)) + 1)
    return dico


def idf(directory):
    noms_fichiers = extract_name_file(files_names)
    dico = {}
    for i in range(Nombre_fichiers):
        name = "Clean_Nomination_" + str(noms_fichiers[i]) + ".txt"
        #print(name)
        with open(directory + name, 'r') as f:
            mot = separation(f.read())
        occurrence = TF(mot)
        #print(occurrence)
        for mot, count in occurrence.items():
            print(occurrence[mot])
            dico[mot] = log((Nombre_fichiers / float(count)) + 1)
            #print(mot, count)
    return dico