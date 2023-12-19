from function import *

"""
# Call of the function list_of_files

directory = "./speeches"
files_names = list_of_files(directory, "txt")
Nombre_fichiers = len(files_names)
#print(files_names)



# Call of the function extract_name
"""
"""
extract_name(files_names)
print(files_names)
"""
"""


extract_name_file(files_names)
for i in range(Nombre_fichiers):        # parcours tous les fichiers du répertoire /speeches
    name = 'Nomination_' + str(files_names[i]) + '.txt'
    with open("./speeches/" + name, 'r') as f1:
        contenue = f1.read()
    contenue = ponctuation(minuscule(contenue))     # convertie le texte du fichier texte en minuscule et supprimer les caractères de ponctuation
    with open("./cleaned/Clean_" + name, 'w') as f2:
        f2.write(contenue)        # stocke le nouveau contenue en minuscule dans un répertoire /cleaned


#print(idf("./cleaned/"))

#print(mots_fichiers("./cleaned/"))
#print(matrice_TF_IDF("./cleaned/"))

"""
"""
# Afficher la liste des mots les moins importants dans le corpus de documents
def mini_TF_IDF(matrice_TF_IDF):
    mini = 0
    l = []
    for i in range(Nombre_fichiers):
        for j in range(Nombre_de_mots):
            if matrice_TF_IDF[i][j] == mini:
                l.append(matrice_TF_IDF[i][j])
    return l

# Afficher la liste des mots les plus importants dans le corpus de documents
def maxi_TF_IDF(matrice_TF_IDF):
    maxi = 0
    l = []
    for i in range(Nombre_fichiers):
        for j in range(Nombre_de_mots):
            if matrice_TF_IDF[i][j] < maxi:
                maxi = matrice_TF_IDF[i][j]
    for i in range(Nombre_fichiers):
        for j in range(Nombre_de_mots):
            if matrice_TF_IDF[i][j] == maxi:
                l.append(matrice_TF_IDF[i][j])
    return l


# mot(s) le(s) plus répété(s) par le président Chirac
directory = "./speeches"
files_names = list_of_files(directory, "txt")
Nombre_fichiers = len(files_names)
extract_name_file(files_names)
print(files_names)

for i in range(Nombre_fichiers):        # parcours tous les fichiers du répertoire /speeches
    if "Chirac" in files_names[i]:      # sélectionner les fichiers du président Chirac
        name = 'Nomination_' + str(files_names[i]) + '.txt'
        with open("./speeches/" + name, 'r') as f1:
            contenue = f1.read()
        contenue = ponctuation(minuscule(contenue))     # convertie le texte du fichier texte en minuscule et supprimer les caractères de ponctuation
        with open("./cleaned/Clean_" + name, 'w') as f2:
            f2.write(contenue)        # stocke le nouveau contenue en minuscule dans un répertoire /cleaned

for i in range(Nombre_fichiers):
    if "Chirac" in files_names[i]:  # sélectionner les fichiers du président Chirac
        name = 'Nomination_' + str(files_names[i]) + '.txt'
        with open("./cleaned/Clean_" + name, 'r') as f:
            contenue = TF(separation(f.read()))
        maxi = 0
        mot_chirac = []
        for mot, count in contenue.items():
            if contenue[mot] < maxi:
                maxi = contenue[mot]
                mot_chirac.append(mot)
print(mot_chirac)
"""
"""


"""

def mot_pas_important(M):
    l=[]
    for i in range(len(M)):
        somme = 0
        for j in range(1,len(M[i])):
            somme += M[i][j]
        if (somme == 0):
            l.append(M[i][0])
    return l

matrice = matrice_tf_idf("./cleaned/")
#print(mot_pas_important(matrice))
"La fonction mot_pas_important est censé marché"


def mot_important(M):
    l=[]
    for i in range(len(M)):
        somme = 0
        for j in range(1,len(M[i])):
            somme += M[i][j]
        if (somme >= 4):
            l.append(M[i][0])
    return l

#print(mot_important(matrice))

def mots_chirac1(matrice_tfidf, seuil=4):
    mots_importants = [mot for mot, score in zip(matrice_tfidf.get_feature_names_out(), matrice_tfidf.data) if score >= seuil]
    mots_importants = sorted(mots_importants, key=lambda mot: matrice_tfidf.get_feature_names_out().index(mot))
    return mots_importants


def mots_chirac(mot_pas_importants, seuil):
    texte = ""
    for i in range(2):
        with open("./cleaned/Clean_Nomination_Chirac" + str(i + 1) + ".txt", 'r') as f:
            texte += f.read()
    texte = separation(texte)
    texte_TF = TF(texte)
    liste = []
    for mot, valeur in texte_TF.items():
        if (valeur >= seuil):
            liste.append(mot)
    return liste


#print(mots_chirac(mot_pas_important(matrice), 4))


def president_nation(tfidf_scores_par_president):
    # Filtrer les présidents qui ont parlé de la "Nation"
    presidents_avec_nation = [president for president, scores in tfidf_scores_par_president.items() if "Nation" in scores]
    # Si aucun président n'a mentionné "Nation", retourner une liste vide
    if not presidents_avec_nation:
        return []
    # Trouver le président qui a le plus mentionné "Nation"
    president_plus_frequent = max(presidents_avec_nation, key=lambda x: tfidf_scores_par_president[x]["Nation"])
    return president_plus_frequent


#print(president_nation(matrice))

def president_ecologie(tfidf_scores_par_president):
    # Filtrer les présidents qui ont parlé du "climat" et/ou de "l'écologie"
    presidents_avec_climat_ecologie = [president for president, scores in tfidf_scores_par_president.items() if "climat" in scores or "écologie" in scores]
    return presidents_avec_climat_ecologie

#print(president_ecologie(matrice))