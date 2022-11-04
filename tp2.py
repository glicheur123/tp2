# Auteur : Marc-Antoine et Alexis Tremblay
# Date : 28/10/2022
# TP#2

import random  # importation de la librairie random pour les nombres aléatoires
from donnees import *  # importe les listes et le dictionnaire du fichier donnees.py

NB_QUESTIONS = 10  # Détermine le nombre de questions

# Noms des créateurs
CREATEURS = "Marc-Antoine Gauthier et Alexis Tremblay"

rejouer = True  # Booléen qui sert à contrôler la boucle pour rejouer

# Conversion des deux listes vers un dictionnaire
capitales_par_pays = {}
for i in range(len(liste_pays)):
    capitales_par_pays[liste_pays[i]] = liste_capitales[i]

while rejouer:
    pointage = 0  # Variable pour le pointage

    # Message de bienvenue
    print("*" * 60)
    print(f"*{'Jeu des capitales':^58}*")
    print(f"*{f'réalisé par {CREATEURS}':^58}*")
    print("*" * 60)

    print("\n\nLe but de ce jeu est de répondre à 10 questions sur les \n"
          "capitales du monde. Allez-vous réussir à battre le record ?")

    input("\nAppuyez sur ENTER pour débuter !")

    nom = ""
    valide = False
    while not valide:
        # Demander le nom du joueur
        nom = input("\nVeuillez entrer votre nom complet : ")  # Demande l'utilisateur d'entrer son nom.
        if nom == "":
            print("Erreur - Le nom ne peut pas être vide.")
        else:
            valide = True

    # Choisir les capitales de cette manche
    pays = random.sample(list(capitales_par_pays.keys()), NB_QUESTIONS)

    # Répondre aux questions
    for question_actuelle, pays_actuel in enumerate(pays):  # Va chercher le pays avec son index dans la liste aléatoire

        print(f"\nQuestion #{question_actuelle+1} : ")  # Affichage du numéro de la question

        # Entre le nom de la capitale
        capitale_utilisateur = input(f"Quelle est la capitale de {pays_actuel} ? : ")

        if capitale_utilisateur.strip().lower() == capitales_par_pays[pays_actuel].strip().lower():
            print("Bravo ! C'est la bonne réponse")
            pointage += 1  # Incrémente le pointage si la réponse est bonne
        else:
            print("Désolé ce n'est pas la bonne réponse")
            print(f"La bonne réponse était : {capitales_par_pays[pays_actuel]}")  # Donne la bonne réponse si mal

    # Affichage du pointage
    print("*" * 51)
    print(f"Vous avez obtenu un pointage de {pointage} sur {NB_QUESTIONS}")

    # Modifier les meilleurs pointages actuels si l'utilisateur est déjà enregistré
    existant = False
    battu = False
    for autre_nom in meilleurs_pointages.keys():
        if autre_nom.strip().lower() == nom.strip().lower():  # Comparer les deux noms en minuscules
            if meilleurs_pointages[autre_nom] < pointage:  # le joueur était déjà présent et il a battu son score
                meilleurs_pointages[autre_nom] = pointage  # Écraser son pointage avec son nouveau record
                battu = True
            existant = True

    # Si le joueur n'a pas été trouvé à l'étape précédente, ajouter son premier pointage
    if not existant:
        meilleurs_pointages[nom] = pointage

    # Trier les meilleurs pointages en une liste par leur score
    classement_noms = sorted(meilleurs_pointages, key=meilleurs_pointages.get, reverse=True)

    top5 = []  # liste des noms trier par les 5 meilleurs en petit caractère et sans espace avant et après.
    for convertion in range(5):
        top5.append(classement_noms[convertion].strip().lower())

    if not battu and existant:  # Le joueur est dans le top 5 et ne s'est pas battu
        print("Vous n'avez pas battu votre meilleur pointage.")
    elif nom.strip().lower() not in top5:  # Le joueur n'est pas dans le top5
        print("Vous n'avez pas battu un des 5 meilleurs pointages.")
    else:  # Le joueur s'est classé dans le top 5, afficher sa position
        print(f"Vous avez obtenu le {top5.index(nom.strip().lower())+1}e meilleur pointage")

    print("*"*51)

    print()

    # Affichange du classement
    # Titres
    print("=" * 44)
    print(f"{'Liste des 5 meilleurs pointages':^44}")
    print("=" * 44)
    print(f"Pos | {'Nom':<25} | Pointage |")
    print("=" * 44)

    for pos, nom in enumerate(top5):
        # Rangée de chaque utilisateur par la liste classement_noms
        print(f"{pos+1}-  | {classement_noms[pos]:<25} | {meilleurs_pointages[classement_noms[pos]]:^8} |")

    # Demander à l'utilisateur s'il veut rejouer
    valide = False
    while not valide:
        choix_utilisateur = input("Voulez-vous rejouer ? (oui/non) : ").strip().lower()

        if choix_utilisateur == "non":
            rejouer, valide = False, True
        elif choix_utilisateur == "oui":
            rejouer, valide = True, True
        else:
            print("Erreur - La réponse doit être oui ou non!")

