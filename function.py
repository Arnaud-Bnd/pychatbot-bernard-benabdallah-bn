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
#with open("./cleaned/Clean_Nomination_Sarkozy.txt", 'r') as f:
    #print(TF(separation((minuscule(f.readline())))))
"La fonction TF fonctionne"


def IDF(directory):     # Score IDF d'un mot, soit l'importance d'un mot dans un ensemble de texte
    dico = {}       # Création du dictionnaire IDF
    files = list_of_files(directory, "txt")     # Liste des noms des fichiers
    for i in range(Nombre_fichiers):
        with open(directory + files[i], 'r', encoding="utf-8") as f:      # Parcours tous les fichiers texte du répertoire
            contenue = TF(separation(f.read()))      # Contenue de chaque fichier sous forme d'un dictionnaire de mot avec leur score TF (occurrence)
        for mot in contenue.keys():         # Parcours les clés du dictionnaire TF, soit tous les mots du texte
            if mot not in dico.keys():
                dico[mot] = 1       # Si le mot n'est pas dans le dictionnaire IDF, alors l'initialiser avec une valeur à 1
            else:
                dico[mot] += 1      # Si le mot est dans le dictionnaire IDF, alors ajouter 1 à sa valeur
    for mot, count in dico.items():
        #print(mot)
        #print(count)
        #print(dico[mot])
        dico[mot] = float(math.log((Nombre_fichiers / count), 10))      # Formule du score IDF
        #print(dico[mot])
        #print()
    return dico


#print(Nombre_fichiers)
print(IDF("./cleaned/"))
"La fonction IDF fonctionne"


def mots_fichiers(directory):         # Créer une liste contenant tous les mots de tous les fichiers
    l = set()       # Créer un set des mots du corpus (tous les textes)
    files = list_of_files(directory, "txt")     # Liste des noms de tous les fichiers
    for i in range(Nombre_fichiers):
        with open(directory + files[i], 'r') as f:        # Ouverture des fichiers texte
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
    files = list_of_files(directory, "txt")     # Liste des noms de chaque fichier
    print(files)
    for mot, IDF_mot in scores_IDF.items():
        tab = []         # Création d'une liste correspondant à une ligne
        tab.append(mot)         # Ajoute le mot à la liste pour savoir quelle ligne correspond à quelle mot
        for j in range(Nombre_fichiers):
            with open(directory + "Clean_" + files_names[j], 'r') as f:      # Parcours tous les fichiers
                contenue = separation(f.read())         # Sépare le texte en liste de mots
                TF_mot = TF(contenue)       # Calcul du dictionnaire des scores TF associés aux mots du texte
                occurrence = TF_mot.get(mot, 0)         # Score TF du mot et s'il est pas dans le dictionnaire alors son TF est 0
                #print(occurrence)
                valeur = round(occurrence * IDF_mot, 2)         # Calcul du vecteur de chaque mot en fonction du fichier
                tab.append(valeur)      # Ajoute la valeur du vecteur TF-IDF à la liste (ligne)
        matrice.append(tab)         # Ajoute la liste (ligne) à la matrice TF-IDF
    return matrice


matrice_TF_IDF = matrice_tf_idf("./cleaned/")
for i in range(len(matrice_TF_IDF)):
    print(matrice_TF_IDF[i])
"La fonction matrice_tf_idf fonctionne"


def question(chaine):       # Sépare la question en mot, tout en enlevant la ponctuation et les majuscules
    liste = separation(ponctuation(minuscule(chaine)))
    return liste


#print(question("Chercher dans le corpus le(s) document(s) le(s) plus pertinent(s),"))
"La fonction question fonctionne"


def question_corpus(liste_question, liste_corpus):      # Créer une liste contenant les mots de la question qui sont aussi dans le corpus de texte
    question_restante = set()       # Création d'un set pour éviter les doublons
    for mot in liste_question:      # Parcours tous les mots de la question
        if mot in liste_corpus:
            question_restante.add(mot)      # Ajoute le mot au set si le mot est également présent de le corpus
    question_restante = list(question_restante)     # Transforme le set en liste
    return question_restante


liste_question = separation("mesdames et messieurs gourde en ce jour où je prends caca officiellement mes oui fonctions de président")

liste_corpus = ""
directory = "./cleaned/"
files = list_of_files(directory, "txt")     # Liste des noms de chaque fichier
for i in range(Nombre_fichiers):
    with open(directory + files[i], 'r') as f:  # Parcours tous les fichiers
        contenue = f.read()
        liste_corpus += contenue
liste_corpus = separation(liste_corpus)
#print(liste_question)
#print(liste_corpus)
question_restante = question_corpus(liste_question, liste_corpus)
#print(question_restante)
"La fonction question_corpus fonctionne"


def question_TF_IDF(liste_question, question_restantes):        # Calcul du vecteur TF-IDF de la question
    # Vecteur TF
    liste_TF = TF(liste_question)       # Calcul du TF (occurrence) de chaque mot de la question
    Score_TF = {}
    for mot, tf in liste_TF.items():      # Parcours les mots de la question
        if mot not in question_restantes:
            Score_TF[mot] = 0       # Si le mot n'est pas dans le corpus, alors sont TF est nul car inintéressant
        else:
            Score_TF[mot] = (tf)       # Sinon, le TF du mot est égale à son occurrence divisée par le nombre de mot de la question
    # Vecteur IDF
    dico_IDF = IDF("./cleaned/")
    Score_IDF = {}
    for mot, value in liste_TF.items():
        if mot in dico_IDF:
            Score_IDF[mot] = dico_IDF[mot]
        else:
            Score_IDF[mot] = 0
    # Vecteur TF-IDF
    vect_TF_IDF = []
    for mot, valeur in Score_TF.items():
        tab = []
        tab.append(mot)
        if mot not in vect_TF_IDF:
            TF_IDF_score = Score_TF[mot] * Score_IDF[mot]
            tab.append(TF_IDF_score)
        vect_TF_IDF .append(tab)
    return vect_TF_IDF


TF_IDF_quest = question_TF_IDF(liste_question, question_restante)
#print(TF_IDF_quest)
"La fonction question_TF_IDF est sensé marcher"


def produit_scalaire(A, B, doc):
    somme = 0
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i][0] == B[j][0]:
                somme += (A[i][1] * B[i][doc])
    return somme


scalaire_quest = produit_scalaire(TF_IDF_quest, matrice_TF_IDF,1)
#print(scalaire_quest)


def norme_vecteur(A):
    somme = 0
    for i in range(len(A)):
        somme += A[i][1] ** 2
    somme = math.sqrt(somme)
    return somme


norme_question = norme_vecteur(TF_IDF_quest)
#print(norme_question)

norme_corpus = norme_vecteur(matrice_TF_IDF)
#print(norme_corpus)

def similarité(A, B, doc):
    res = produit_scalaire(A, B, doc) / (norme_vecteur(A) * norme_vecteur(B))
    return res


#for i in range(8):
    #print(similarité(TF_IDF_quest, matrice_TF_IDF,i + 1))

#print(files_names)

def plus_pertinent(matrice, tf_idf_quest, file_name):
    pass