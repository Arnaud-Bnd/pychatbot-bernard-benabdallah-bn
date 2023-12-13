import math
import os


def list_of_files(directory, extension):
    files_names = []        # Créer une liste qui va contenir les noms des fichiers
    for filename in os.listdir(directory):
        if filename.endswith(extension):        # Selection seulement les fichiers textes
            files_names.append(filename)        # Ajoute les noms des fichiers textes à la liste files_names
    return files_names


# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
Nombre_fichiers = len(files_names)


# Extraire nom président
def extract_name(liste):        # Extrait seulement le nom de chaque président à partir du nom des fichiers textes
    for i in range(len(liste)):
        liste[i] = liste[i][11:-4]      # Enlève le "Nomination_" et le ".txt"
        if '1' in liste[i] or '2' in liste[i]:
            liste[i] = liste[i][:-1]        # Enlève le "1" et le "2" s'il y a plusieurs fichiers pour un même président
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
def extract_name_file(liste):       # Extrait le nom du président et le numéro s'il y en a un (sera utile pour parcours les fichiers)
    for i in range(len(liste)):
        liste[i] = liste[i][11:-4]
    return liste


# Mettre en minuscule
def minuscule(mot):     # Met tous les caractères alphabétiques en minuscule
    nouveau_mot = ""        # Créer une nouvelle chaîne de caractère pour conserver l'ancienne
    nouveau_mot = list(nouveau_mot)     # Convertie la chaîne de caractère en liste
    mot = list(mot)     # Convertie la chaîne de caractère en liste
    for i in range(len(mot)):
        if (ord('A') <= ord(mot[i])) and (ord(mot[i]) <= ord('Z')):     # Sélectionne uniquement les caractères en majuscule
            mot[i] = chr(ord(mot[i]) + (ord('a') - ord('A')))       # Conversion en minuscule
        nouveau_mot.append(mot[i])      # Ajoute à la nouvelle chaîne de caractère
    return ''.join(nouveau_mot)     # Reconvertie la liste en chaîne de caractère


#print(minuscule("TEST"))
"La fonction minuscule fonctionne"


def ponctuation(mot):       # Supprime tous les signes de ponctuation d'une chaîne de caractère
    nouveau_mot = ""        # Créer une nouvelle chaîne de caractère sans les ponctuations
    pas_permis = '!#"$%&()*+,./:;<=>?@[\]^{|}≈~-_—–\n'
    apostrophe_list = "'’‘"
    for i in range(len(mot)):
        if mot[i] in pas_permis:
            mot_clean1 = " "
            nouveau_mot += mot_clean1
        elif mot[i] in apostrophe_list:        # Sélectionne uniquement les apostrophes et les tirets
            var = random.randint(1,2)
            if (mot[i-1] != ord('l')) or (var % 2 == 0):
                mot_clean2 = 'e '
                nouveau_mot += mot_clean2
            else:
                mot_clean3 = 'a '
                nouveau_mot += mot_clean3
        else:
            nouveau_mot += mot[i]
    return nouveau_mot     # Reconvertie la liste en chaîne de caractère


#print(ponctuation("J'en peux plus, je comprends@ pas pourquoi ça ne marche pas ce code de merde"))
"La fonction ponctuation fonctionne"


def separation(chaine):     # Prend en paramètre une chaîne de caractère et renvoie une liste de mot
    l = []
    mot = ""
    for caractere in chaine:
        if (caractere != ' '):      # Sélectionne tous les caractères jusqu'à un espace
            mot += caractere        # Ajoute les caractères sélectionnés à une chaine de caractère
        elif mot:       # Délimite le mot
            l.append(mot)       # Si le mot n'est pas dans la chaine de caractère, l'ajouter à la liste
            mot = ""        # Réinitialise la chaine de caractère
    if mot:     # Prise en compte du dernier mot
        l.append(mot)       # Si la chaîne ne se termine pas part un espace, alors le dernier mot est ajouter
    return l


#print(separation(minuscule("Je en peux plus je comprends pas pourquoi ça ne marche pas ce code de merde")))
"La fonction separation fonctionne"


def TF(liste):      # Score TF d'un mot, soit l'occurrence d'un mot dans un texte préalablement transformer en liste de mot
    dico = {}       # Création du dictionnaire IDF
    for i in range(len(liste)):
        if liste[i] not in dico:
            dico[liste[i]] = 1       # Si le mot n'est pas dans la chaine de caractère, l'ajouter au dictionnaire assiocié à une valeur 1
        else:
            dico[liste[i]] += 1      # Sinon ajouter 1 à la valeur associée au mot
    return dico


#print(TF(separation(minuscule("Je en peux plus je comprends pas pas pourquoi pas ça ne marche pas ce code de merde"))))
"La fonction TF fonctionne"


def IDF(directory):     # Score IDF d'un mot, soit l'importance d'un mot dans un ensemble de texte
    dico = {}       # Création du dictionnaire IDF
    files = list_of_files(directory, "txt")     # Liste des noms des fichiers
    for i in range(Nombre_fichiers):
        with open(directory + files[i], 'r') as f:      # Parcours tous les fichiers texte du répertoire
            contenue = TF(separation(f.read()))      # Contenue de chaque fichier sous forme d'un dictionnaire de mot avec leur score TF (occurrence)
        for mot in contenue.keys():         # Parcours les clés du dictionnaire TF, soit tous les mots du texte
            if mot not in dico.keys():
                dico[mot] = 1       # Si le mot n'est pas dans le dictionnaire IDF, alors l'initialiser avec une valeur à 1
            else:
                dico[mot] += 1      # Si le mot est dans le dictionnaire IDF, alors ajouter 1 à sa valeur
    for mot, count in dico.items():
        dico[mot] = float(math.log((Nombre_fichiers / count), 10))      # Formule du score IDF
    return dico


#print(Nombre_fichiers)
#print(IDF("./cleaned/"))
"La fonction IDF fonctionne"


def mots_fichiers(directory,l):         # Créer une liste contenant tous les mots de tous les fichiers
    files = list_of_files(directory, "txt")     # Liste des noms de tous les fichiers
    for i in range(Nombre_fichiers):
        if (i == 0):
            with open(directory + files[i], 'r') as f:        # Ouverture du premier fichier texte
                contenue = separation(f.read())     # Transforme le texte du fichier en liste de mot
            for j in range(len(contenue)):
                l.append(contenue[j])       # Ajoute tous les mots du premier fichier à la liste
        else:
            with open(directory + files[i], 'r') as f:        # Ouverture des autres fichiers texte
                contenue = separation(f.read())     # Transforme le texte du fichier en liste de mot
            for j in range(len(contenue)):      # Parcours la liste de mots
                if contenue[j] not in l:
                    l.append(contenue[j])       # Si le mot n'est pas déjà dans la liste, il est ajouté
    return l


liste_mots = []
#print(mots_fichiers("./cleaned/",liste_mots))
"La fonction mots_fichiers fonctionne"


def matrice_tf_idf2(directory):
    dico_IDF = IDF(directory)       # Dictionnaire des scores IDF de chaque mot
    files = list_of_files(directory, "txt")     # Liste des noms de chaque fichier
    matrice = []        # Création de la matrice TF-IDF
    for i in dico_IDF:
        mot_IDF = i        # Correspond à chaque mot de tous les fichiers (présent dans le dictionnaire IDF)
        score_IDF = dico_IDF[i]       # Score IDF de chaque mot de tous les fichiers
        tab = []
        occurrence = 0
        for j in range(Nombre_fichiers):
            with open(directory + files[j], 'r') as f:      # Parcours tous les fichiers texte
                contenue = separation(f.read())         # Transforme le contenue du fichier en liste de mots
            TF_mot = TF(contenue)       # Calcul du score TF des mots du fichier texte
            #print(TF_mot)
            for k in TF_mot:
                mot_TF = k      # Correspond au mot présent dans le fichier ouvert (présent dans le dictionnaire TF)
                if (mot_TF == mot_IDF):      # Si le mot est à la fois dans les dictionnaires IDF et TF
                    occurrence += 1      # Alors ajoute
                    print(occurrence)
            if mot_IDF not in TF_mot:
                occurrence = 0
            valeur = round(occurrence * score_IDF, 2)
            tab.append(valeur)
        matrice.append(tab)
    return matrice


def matrice_tf_idf(directory):
    scores_IDF = IDF(directory)
    files = list_of_files(directory, "txt")     # Liste des noms de chaque fichier
    matrice = []

    for mot, IDF_mot in scores_IDF.items():
        tab = []
        for j in range(Nombre_fichiers):
            with open(directory + files[j], 'r') as f:
                contenue = separation(f.read())
                TF_mot = TF(contenue)
                occurrence = TF_mot.get(mot, 0)
                valeur = round(occurrence * IDF_mot, 2)
                tab.append(valeur)
        matrice.append(tab)

    return matrice


matrice = matrice_tf_idf2("./cleaned/")
#for i in range(len(matrice)):
    #print(matrice[i])


def question(chaine):       # Sépare la question en mot, tout en enlevant la ponctuation et les majuscules
    liste = separation(ponctuation(minuscule(chaine)))
    return liste


#print(question("Chercher dans le corpus le(s) document(s) le(s) plus pertinent(s),"))
"La fonction question fonctionne"


def question_corpus(liste_question, liste_corpus):
    question_restante = []
    for mot in liste_question:
        if (mot in liste_corpus) and (mot not in question_restante):
            question_restante.append(mot)
    return question_restante


liste_question = separation("messieurs les présidents gourde mesdames messieurs en ce jour où je prends")
liste_corpus = separation("messieurs les présidents mesdames messieurs en ce jour où je prends")
#print(question_corpus(liste_question, liste_corpus))
"La fonction question_corpus fonctionne"


def question_TF_IDF(liste_question, question_restantes):
    liste_TF = TF(liste_question)
    #print(liste_TF)
    #print(len(liste_question))
    for mot in question_restantes:
        #print(liste_TF[mot]/12)
        liste_TF[mot] = liste_TF[mot]/12
        if mot not in question_restantes:
            liste_TF[mot] = 0
        #else:
            #liste_TF[mot] = (liste_TF[mot])/(len(liste_question))
    return liste_TF


question_restante = question_corpus(liste_question, liste_corpus)
#print(question_TF_IDF(liste_question, question_restante))


#print(mots_fichiers("./cleaned/",liste_mots))
#question = question("messieurs les présidents gourde mesdames messieurs en ce jour où je prends")
#print(question)
#corpus = question("messieurs les présidents gourde en ce jour où je prends")
#print(corpus)
#print(in_corpus(question, corpus))

import random


def ponctuation2(mot):
    nouveau_mot = ""
    pas_permis = "!#\"$%&()*+,./:;<=>?@[\\]^{|}≈~-_—–\n"
    apostrophe_list = "'’`‘"

    for i in range(len(mot)):
        if mot[i] in pas_permis:
            continue
        elif mot[i] in apostrophe_list and i > 0:  # Vérifie si c'est une apostrophe et si elle n'est pas en première position
            var = random.randint(1, 2)
            if (mot[i - 1] != 'l') or (var % 2 == 0):
                nouveau_mot += 'e'
            else:
                nouveau_mot += 'a'
        else:
            nouveau_mot += mot[i]
    return nouveau_mot


#print(ponctuation2("J'en peux plus, je comprends@ pas pourquoi ça ne marche pas ce code de merde"))

