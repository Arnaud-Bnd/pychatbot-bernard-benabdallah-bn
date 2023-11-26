from function import *


# Call of the function list_of_files

directory = "./speeches"
files_names = list_of_files(directory, "txt")
Nombre_fichiers = len(files_names)
#print(files_names)



# Call of the function extract_name
"""
extract_name(files_names)
print(files_names)
"""


extract_name_file(files_names)
for i in range(Nombre_fichiers):        # parcours tous les fichiers du répertoire /speeches
    name = 'Nomination_' + str(files_names[i]) + '.txt'
    with open("./speeches/" + name, 'r') as f1:
        contenue = f1.read()
    contenue = ponctuation(minuscule(contenue))     # convertie le texte du fichier texte en minuscule et supprimer les caractères de ponctuation
    with open("./cleaned/Clean_" + name, 'w') as f2:
        f2.write(contenue)        # stocke le nouveau contenue en minuscule dans un répertoire /cleaned



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