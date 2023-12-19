import math
import os
import random


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


# Créer un dictionnaire qui associe un prénom au nom du président
prenom_nom = {'Chirac' : 'Jacques',
              'Mitterrand' : 'François',
              'Sarkozy' : 'Nicolas',
              'Macron' : 'Emmanuel',
              'Giscard dEstaing' : 'Valéry',
              }


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
#with open("./cleaned/Clean_Nomination_Sarkozy.txt", 'r') as f:
    #print(TF(separation((minuscule(f.readline())))))
"La fonction TF fonctionne"


def IDF(directory):     # Score IDF d'un mot, soit l'importance d'un mot dans un ensemble de texte
    dico = {}       # Création du dictionnaire IDF
    for i in range(Nombre_fichiers):
        with open(directory + "Clean_" + files_names[i], 'r', encoding="utf-8") as f:      # Parcours tous les fichiers texte du répertoire
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


def mots_fichiers(directory):         # Créer une liste contenant tous les mots de tous les fichiers
    l = set()       # Créer un set des mots du corpus (tous les textes)
    for i in range(Nombre_fichiers):
        with open(directory + "Clean_" + files_names[i], 'r') as f:        # Ouverture des fichiers texte
            contenue = separation(f.read())     # Transforme le texte du fichier ouvert en liste de mot
        for mot in contenue:
            l.add(mot)       # Ajoute tous les mots du fichier ouvert à la liste de mot
    l = list(l)
    return l


liste_mots = (mots_fichiers("./cleaned/"))
#print(liste_mots)
"La fonction mots_fichiers fonctionne"


def matrice_tf_idf(directory):
    matrice = []        # Création de la matrice TF-IDF
    scores_IDF = IDF(directory)
    for mot, IDF_mot in scores_IDF.items():
        tab = []         # Création d'une liste correspondant à une ligne
        tab.append(mot)         # Ajoute le mot à la liste pour savoir quelle ligne correspond à quelle mot
        for j in range(Nombre_fichiers):
            with open(directory + "Clean_" + files_names[j], 'r') as f:      # Parcours tous les fichiers
                contenue = separation(f.read())         # Sépare le texte en liste de mots
                TF_mot = TF(contenue)       # Calcul du dictionnaire des scores TF associés aux mots du texte
                occurrence = TF_mot.get(mot, 0)         # Score TF du mot et s'il est pas dans le dictionnaire alors son TF est 0
                valeur = round(occurrence * IDF_mot, 2)         # Calcul du vecteur de chaque mot en fonction du fichier
                tab.append(valeur)      # Ajoute la valeur du vecteur TF-IDF à la liste (ligne)
        matrice.append(tab)         # Ajoute la liste (ligne) à la matrice TF-IDF
    return matrice


#matrice_TF_IDF = matrice_tf_idf("./cleaned/")
#for i in range(len(matrice_TF_IDF)):
    #print(matrice_TF_IDF[i])
"La fonction matrice_tf_idf fonctionne"


def question_propre(chaine):       # Sépare la question en mot, tout en enlevant la ponctuation et les majuscules
    liste = separation(ponctuation(minuscule(chaine)))
    return liste


#print(question_propre("Chercher dans le corpus le(s) document(s) le(s) plus pertinent(s),"))
"La fonction question_propre fonctionne"


def intersection_question(question, matrice):      # Créer une liste contenant les mots de la question qui sont aussi dans le corpus de texte (donc dans la matrice TF-IDF)
    liste_question = question_propre(question)
    question_restante = set()       # Création d'un set pour éviter les doublons
    for mot in liste_question:      # Parcours tous les mots de la question
        for i in range(len(matrice)):
            if (mot == matrice[i][0]):      # Le mot est situé à l'index 0 de chaque ligne
                question_restante.add(mot)      # Ajoute le mot au set si le mot est également présent dans le corpus
    question_restante = list(question_restante)     # Transforme le set en liste
    return question_restante


def intersection_corpus(question_restante, matrice):     # Créer une liste contenant les scores TF-IDF des mots du corpus aussi présent dans la question
    corpus_restant = []     # Création d'une liste qui contiendra les scores TF-IDF
    for i in range(len(matrice)):       # Parcours de chaque ligne de la matrice TF-IDF du corpus
        if matrice[i][0] in question_restante:      # Le mot est situé à l'index 0 de chaque ligne
            corpus_restant.append(matrice[i])       # Si le mot est dans la question, alors ses scores TF-IDF sont ajoutés à la liste
    return corpus_restant


question = "Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"
#liste_question = question_propre("Peux-tu me dire comment une nation peut-elle prendre soin du climat ?")
#print(liste_question)


def corpus_global(directory):       # Prend en paramètre un répertoire et renvoie l'ensemble du corpus sous forme d'une liste de mots
    corpus = ""     # Chaine de caractères qui contiendra tous les textes
    files = list_of_files(directory, "txt")     # Liste des noms de chaque fichier
    for i in range(Nombre_fichiers):
        with open(directory + files[i], 'r') as f:  # Parcours tous les fichiers
            contenue = f.read()
            corpus += contenue      # Le contenue est ajouté à la chaine de caractère commune à tous les textes
    corpus = separation(corpus)     # Transforme la chaine de caractères en liste de mot
    return corpus


corpus = corpus_global("./cleaned/")
#print(corpus)
"La fonction corpus_global fonctionne"

#matrice_TF_IDF = matrice_tf_idf("./cleaned/")
#question_restante = intersection_question(question, matrice_TF_IDF)
#corpus_restant = intersection_corpus(question_restante, matrice_TF_IDF)
#print(question_restante)
#print(corpus_restant)
"Les fonctions intersection_question et intersection_corpus fonctionnent"


def question_TF_IDF(question):        # Calcul du vecteur TF-IDF de la question
    liste_question = question_propre(question)
    matrice_TF_IDF = matrice_tf_idf("./cleaned/")
    question_restantes = intersection_question(question, matrice_TF_IDF)
    # Vecteur TF
    liste_TF = TF(liste_question)       # Calcul du TF (occurrence) de chaque mot de la question
    Score_TF = {}
    for mot, tf in liste_TF.items():      # Parcours les mots de la question
        if mot in question_restantes:
            Score_TF[mot] = (tf)       # Si le mot est dans question_restante (donc dans le corpus), alors le TF du mot est égale à son occurrence dans la question
    # Vecteur IDF
    dico_IDF = IDF("./cleaned/")        # Calcul du score IDF du corpus
    Score_IDF = {}
    for mot, value in liste_TF.items():     # Récupérer les mots et leurs scores TF
        if mot in dico_IDF:
            Score_IDF[mot] = dico_IDF[mot]      # Si le mot est dans le dictionnaire IDF (donc dans le corpus), ajouter le mot et sa valeur de Score_IDF
        else:
            Score_IDF[mot] = 0      # Sinon associé 0 au mot, car il n'est pas dans le corpus
    # Vecteur TF-IDF
    vect_TF_IDF = []
    for mot, valeur in Score_TF.items():
        tab = []        # Création d'une liste qui correspondera à une ligne (un mot)
        tab.append(mot)     # Ajouter le mot à la ligne
        if mot not in vect_TF_IDF:
            TF_IDF_score = Score_TF[mot] * Score_IDF[mot]       # Si le mot n'est pas encore dans vect_TF_IDF, calculer son TF_IDF dans la question
            tab.append(TF_IDF_score)        # Ajouter son score à la ligne
        vect_TF_IDF .append(tab)        # Ajouter la ligne au vecteur TF-IDF de la question
    return vect_TF_IDF


TF_IDF_quest = question_TF_IDF(question)
#print(TF_IDF_quest)
"La fonction question_TF_IDF est censée marcher"


def produit_scalaire(A, B, doc):        # Prends en paramètre le vecteur de la question et la matrice du corpus préalablement mis à la même taille
    somme = 0       # Initialise une somme à 0
    for i in range(len(A)):     # Parcours les lignes de la question
        for j in range(len(B)):     # Parcours les lignes de la matrice
            if A[i][0] == B[j][0]:      # Si le mot de la ligne du vecteur de la question est le même que celui de la ligne de la matrice
                somme += (A[i][1] * B[i][doc])      # Multiplie leur score TF-IDF et les ajoute à la somme
    return somme

#matrice_TF_IDF = matrice_tf_idf("./cleaned/")
#matrice_TF_IDF_restante = intersection_corpus(intersection_question(question, matrice_TF_IDF), matrice_TF_IDF)
#scalaire_quest = produit_scalaire(TF_IDF_quest, matrice_TF_IDF_restante,1)
#print(scalaire_quest)
"La fonction produit_scalaire est censée fonctionner"


def norme_vecteur(A, doc):      # Prend en paramètre un vecteur et le document souhaité (la colonne), doc = 1 pour la question car il n'y a pas d'autre document
    somme = 0       # Initialise une somme à 0
    for i in range(len(A)):     # Parcours les lignes du vecteur
        somme += A[i][doc] ** 2     # Met au carré le score TF-IDF du mot et l'ajoute à la somme
    somme = math.sqrt(somme)        # Fait la racine carré de la somme
    return somme


norme_question = norme_vecteur(TF_IDF_quest, 1)
#print(norme_question)
"La fonction norme_vecteur fonctionne pour le vecteur de la question"


#for i in range(len(files_names)):
    #norme_corpus = norme_vecteur(matrice_TF_IDF_restante, i + 1)
    #print(files_names[i])
    #print(norme_corpus)
    #print()
"La fonction norme_vecteur fonctionne pour les vecteurs de la matrice"


def similarite(A, B, doc):      # Calcul de la similarité en prenant en paramètre les vecteurs de la question et de la matrice (préalablement mis à la même taille)
    res = produit_scalaire(A, B, doc) / (norme_vecteur(A, 1) * norme_vecteur(B, doc))       # Divise le produit scalaire par le produit des normes des vecteurs
    return res


#for i in range(8):
    #similarite_doc = similarité(TF_IDF_quest, matrice_TF_IDF_restante,i + 1)
    #print(files_names[i])
    #print(similarite_doc)
    #print()
"La fonction similarité est censée fonctionner"


def plus_pertinent(matrice, tf_idf_quest, liste_noms_fichiers):
    plus_similaire = ""
    maxi = 0        # Initialisation d'un maximum à 0
    for i in range(len(liste_noms_fichiers)):       # Parcours chaque document du répertoire
        similaire = similarite(tf_idf_quest, matrice, i + 1)        # Calclul de la similarité avec le document document (La première colonne correspond au mot d'où le i+1)
        if (maxi < similaire):      #  Si le maximum est inférieur à la similarité du document
            maxi = similaire        # le maximum devient égal à la similarité du document
            plus_similaire = liste_noms_fichiers[i]     # Stockage du nom du fichier avec la plus grand similarité dans plus_similaire
    return plus_similaire


#TF_IDF_quest1 = question_TF_IDF(question)
#print(TF_IDF_quest1)
#most_pertinent = plus_pertinent(matrice_TF_IDF_restante, TF_IDF_quest1, files_names)
#print(most_pertinent)


def reponse(question, plus_similaire):      # Détermine la réponse à partir de la question et du document le plus similaire
    # Mot avec le score TF-IDF le plus élevé
    tf_idf_question = question_TF_IDF(question)     # Calcul du vecteur TF-IDF de la question
    res = ""        # Initialisation du résultat
    maxi = 0        # Initialisation d'un maximum à 0
    for i in range(len(tf_idf_question)):       # Parcours chaques lignes du vecteur TF-IDF de la question
        if (maxi < tf_idf_question[i][1]):      # Si le score TF-IDF du mot est supérieur au maximum
            maxi = tf_idf_question[i][1]        # Le maximum devient égal à la nouvelle valeur la plus élevée
            res = tf_idf_question[i][0]     # Stockage du mot avec le score TF-IDF le plus élevé dans la variable res
    # Phrase contenant le mot
    with open("./speeches/" + plus_similaire, 'r') as f:        # Ouverture du document le plus similaire
        contenue = f.read()     # Stockage de son conetnue
    phrase_interessante = ""
    phrase = ""
    i = 0
    while i < len(contenue):        # Parcours chaque caractère du contenue du fichier
        if (contenue[i] != '.'):
            phrase += contenue[i]       # Si le caractère n'est pas un point, ajoute le caractère à phrase
        else:
            phrase += contenue[i]       # Sinon ajoute le point à la fin de la phrase
            phrase_propre = question_propre(phrase)     # Transformation de la phrase en liste de mots sans majuscules ni ponstuations
            if "climat" in phrase_propre:       # Si climat est dans la liste de mots de la phrase
                phrase_interessante = phrase[1:]        # Stockage de la phrase qui nous intéresse ([1:] car il y a des \n
                i += len(contenue) - i      # Mettre fin à la booucle while une fois la phrase qui nous intéresse est trouvé
            phrase = ""     # Réinitialisé la phrase à 0
        i += 1      # Incrémentation de i
    return res, phrase_interessante


#print(reponse(question, "Nomination_Macron.txt"))
"La fonction réponse fonctionne"


question_starter = {"comment": "Après analyse, ",
                    "pourquoi": "Car, ",
                    "peux-tu": "Oui, bien sûr ! "}


def affiner_reponse(question, phrase_reponse):      # Ajout de réplique à la réponse
    phrase_reponse = list(phrase_reponse)       # Transforme phrase_réponse (tuple) en liste
    liste_question = question_propre(question)      # Transforme la question en liste de mots sans ponctuations ni majuscules
    for mot in liste_question:      # Parcours des mots de la question
        if mot in question_starter:     # Si le mot fait partie du dictionnaire de starter de question
            phrase_reponse[1] = list(phrase_reponse[1])     # Transforme la phrase réponse en liste de mot
            phrase_reponse[1][0] = chr(ord(phrase_reponse[1][0]) + (ord('a') - ord('A')))       # Convertie la première lettre de la phrase réponse en minuscule
            phrase_reponse[1] = ''.join(phrase_reponse[1])      # Reconvertie la phrase réponse en chaîne de caractères
            phrase_reponse[1] = question_starter[mot] + phrase_reponse[1]       # Ajoute à la phrase réponse la réplique associé au starter de la question
    return phrase_reponse[1]        # Retourne seulement la phrase réponse sans le mot le plus pertinent

#print(affiner_reponse(question, reponse(question, "Nomination_Macron.txt")))
