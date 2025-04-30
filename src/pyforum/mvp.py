# Importation des classes nécessaires
from time import sleep
from pyforum.bd import BD
import tkinter as tk



def afficher_menu():
    #"""Affiche les options du menu."""
    #print("\n---- Menu ----")
    #print("1. Créer un utilisateur")
    #print("2. Créer un forum")
    #print("3. Créer une publication")
    #print("4. Ajouter un commentaire à une publication")
    #print("5. Joindre un forum")
    #print("6. Quitter")
    
    root = tk.Tk()
    root.title("Pyforum")

    # Création des frames
    en_tete = tk.Frame(root, bg="lightgray")
    en_tete.pack(fill="both", expand=True)

    # Création des variables
    choix = tk.IntVar(root, None)

    # Établissement des fonctions


    # Création d'un étiquette pour donnner les choix à l'utilisateur
    label_options = tk.Label(en_tete, width= 200, text="Veuillez entrer une option : " \
    "\n1. Créer un utilisateur "
    "\n2. Créer un forum "
    "\n3. Créer une publication "
    "\n4. Ajouter un commentaire à une publication "
    "\n5. Joindre un forum "
    "\n6. Quitter ", font=("Arial", 16),borderwidth=2, relief="solid")
    label_options.pack(padx=20, pady=10)

    # Création d'une entrée pour que l'utilisateur entre un choix
    entry = tk.Entry(en_tete, textvariable=choix, width=150, borderwidth=20, font=("Arial", 16))
    entry.pack()

    # Création d'un bouton pour que l'utilisateur confirme son choix
    button1 = tk.Button(en_tete, text="Confirmer", font=("Arial", 16), width=25, height=2, borderwidth=20, bg="orange")
    button1.pack(pady=15)

    # Création des frames d'en bas
    option1 = tk.Frame(en_tete, borderwidth=5, relief="solid", width=317, height=50)

    # Titre de l'option
    titre_option1 = tk.Label(option1, text="Création d'un utilisateur", font=("Arial", 16))
    titre_option1.pack(pady=3)

    # Création d'entrée dans la frame pour le nom d'utilisateur
    label_nomUtilisateur = tk.Label(option1, text="Entrez votre nom d'utilisateur", font=("Arial", 12))
    label_nomUtilisateur.pack()

    nomUtilisateur = tk.Entry(option1)
    nomUtilisateur.pack(pady=3)

    # Création d'entrée dans la frame pour l'adresse Email
    label_adresseEmail = tk.Label(option1, text="Entrez votre adresse Email", font=("Arial", 12))
    label_adresseEmail.pack()

    adresseEmail = tk.Entry(option1)
    adresseEmail.pack(pady=3)

    # Création d'entrée dans la frame pour le mot de passe
    label_motdepasse = tk.Label(option1, text="Entrez votre mot de passe", font=("Arial", 12))
    label_motdepasse.pack()

    adresseEmail = tk.Entry(option1)
    adresseEmail.pack(pady=3)

    # Création d'un boutton pour confirmer les entrées
    bouton_option1 = tk.Button(option1, text="Confirmer", width=20, height=7)
    bouton_option1.pack(pady=3)

    option1.pack(side="left", fill="both", expand=True)

    option2 = tk.Frame(en_tete, borderwidth=5, relief="solid", width=317, height=50)
    option2.pack(side="left", fill="both", expand=True)

    option3 = tk.Frame(en_tete, borderwidth=5, relief="solid", width=317, height=50)
    option3.pack(side="left", fill="both", expand=True)

    option4 = tk.Frame(en_tete, borderwidth=5, relief="solid", width=317, height=50)
    option4.pack(side="left", fill="both", expand=True)

    option5 = tk.Frame(en_tete, borderwidth=5, relief="solid", width=317, height=50)
    option5.pack(side="left", fill="both", expand=True)

    option6 = tk.Frame(en_tete, borderwidth=5, relief="solid", width=317, height=50)
    option6.pack(side="left", fill="both", expand=True)

    #if choix.get() == 1:

        

    
    root.mainloop()
    


def main():

    bd1 = BD( )

    while True:

        # Demander à l'utilisateur de choisir une option valide
        try:
            choix = int(input("Choisissez une option (1-6): "))
        except ValueError:
            print("Veuillez entrer une valeur valide")
            continue

        if choix == 1:
            # Créer un utilisateur
            print("\nCréation d'un utilisateur...")
            nomUtilisateur = input("Entrez le nom d'utilisateur: ")
            adresseEmail = input("Entrez votre adresse email: ")
            motDePasse = input("Entrez votre mot de passe: ")
            listeDeForums = []

            # Sauvegarde l'utilisateur dans la base de données
            bd1.creer_utilisateur(nomUtilisateur, adresseEmail, motDePasse, listeDeForums)
            print(f"L'utilisateur {nomUtilisateur} a été créé avec succès!")


        elif choix == 2:
            # Créer un forum
            print("\nCréation d'un forum...")
            nomForum = input("Entrez le nom du forum: ")
            descriptionForum = input("Entrez une description du forum: ")
            listePublications = []

            # Demande à l'utilisateur ses informations
            nomUtilisateurForum = input("Entrez votre nom d'utilisateur: ")

            # Vérifie si l'utilisateur existe dans la base de données
            utilisateur_trouve = bd1.obtenir_utilisateur_par_nom(nomUtilisateurForum)

            if utilisateur_trouve:

                # Crée le forum
                bd1.creer_forum(nomForum, descriptionForum, listePublications, utilisateur_trouve)

                print(f"Le forum {nomForum} a été créé avec succès et ajouté à votre liste de forums.")
            else:
                print("Nom d'utilisateur introuvable. Veuillez entrer un nom d'utilisateur valide ou vous créer un compte.")


        elif choix == 3:
            # Créer une publication
            print("\nCréation d'une publication...")
            titrePublication = input("Entrez le titre de la publication: ")
            contenuPublication = input("Entrez le contenu de la publication: ")
            dateCreation = input("Entrez la date d'ajourd'hui: ")
            listeCommentaires = []
            identifiantAuteur = None
            identifiantForumAuteur = None

            # Demande à l'utilisateur ses informations
            nomUtilisateurPublication = input("Entrez votre nom d'utilisateur: ")
            nomForumPublication = input("Entrez le nom du forum dont vous souhaiter faire une publication: ")


            # Vérifie si l'utilisateur existe dans la base de données
            utilisateur_trouve = bd1.obtenir_utilisateur_par_nom(nomUtilisateurPublication)

            # Vérifie si le forum existe dans la base de données
            forum_trouve = bd1.obtenir_forum_par_nom(nomForumPublication)

            if utilisateur_trouve and forum_trouve:
                # Vérifie si l'utilisateur est membre du forum
                if forum_trouve.nomForum not in utilisateur_trouve.listeDeForums:
                    print("Vous devez être membre de ce forum pour publier.")
                    continue

                # Trouve l'identifiant de l'utilisateur
                identifiantAuteur = utilisateur_trouve.new_id_utilisateur

                # Trouve l'identifiant du forum
                identifiantForumAuteur = forum_trouve.new_id_forum

                # Crée la publication
                bd1.creer_publication(titrePublication, contenuPublication, dateCreation, identifiantAuteur, identifiantForumAuteur, listeCommentaires, forum_trouve)

                print(f"La publication {titrePublication} a été créé avec succès!")
            else:
                print("Nom d'utilisateur ou forum introuvable. Veuillez entrer un forum ou nom d'utilisateur valide.")
                


        elif choix == 4:
            # Ajouter un commentaire
            print("\nAjouter un commentaire...")
            contenuCommentaire = input("Entrez le contenu du commentaire: ")
            identifiantAuteur = None
            identifiantPublication = None

            # Demande à l'utilisateur ses informations
            nomUtilisateurCommentaire = input("Entrez votre nom d'utilisateur: ")
            nomForumCommentaire = input("Entrez le nom du forum dont vous souhaitez commenter: ")
            nomPublicationCommentaire = input("Entrez le titre de la publication dont vous souhaitez commenter: ")


            # Vérifie si l'utilisateur existe dans la base de données
            utilisateur_trouve = bd1.obtenir_utilisateur_par_nom(nomUtilisateurCommentaire)

            # Vérifie si le forum existe dans la base de données
            forum_trouve = bd1.obtenir_forum_par_nom(nomForumCommentaire)

            # Vérifie si la publication existe dans la base de données
            publication_trouve = bd1.obtenir_publication_par_titre(nomPublicationCommentaire)

            if utilisateur_trouve and forum_trouve and publication_trouve:
                # Vérifie si l'utilisateur est membre du forum
                if forum_trouve.nomForum not in utilisateur_trouve.listeDeForums:
                    print("Vous devez être membre de ce forum pour publier.")
                    continue

                # Trouve l'identifiant de l'utilisateur
                identifiantAuteur = utilisateur_trouve.new_id_utilisateur

                # Trouve l'identifiant de la publication concernée
                identifiantPublication = publication_trouve.new_id_publication

                # Crée le commentaire
                bd1.creer_commentaire(contenuCommentaire, identifiantAuteur, identifiantPublication, publication_trouve)

                print("Commentaire créé avec succès!")
            else:
                print("Utilisateur, forum ou publication introuvable. Veuillez entrer un forum, un nom d'utilisateur ou une publication valide.")



        elif choix == 5:
            # Joindre un forum
            print("\nJoindre un forum...")
            nomUtilisateurJoindreForum = input("Entrez votre nom d'utilisateur: ")
            nomForumJoindreForum = input("Entrez le nom du forum que vous souhaitez joindre: ")

            # Vérifie si l'utilisateur existe dans la base de données
            utilisateur_trouve = bd1.obtenir_utilisateur_par_nom(nomUtilisateurJoindreForum)

            # Vérifie si le forum existe dans la base de données
            forum_trouve = bd1.obtenir_forum_par_nom(nomForumJoindreForum)

            if utilisateur_trouve and forum_trouve:
                
                # Ajoute l'utilisateur au forum correspondant
                bd1.joindre_forum(utilisateur_trouve, forum_trouve)

                print("Vous avez rejoint le forum avec succès!")
            else:
                print("Nom d'utilisateur ou forum introuvable. Veuillez entrer un forum ou nom d'utilisateur valide.")


        elif choix == 6:
            # Quitter le programme
            print("\nMerci d'avoir utilisé PyForum. À bientôt!")
            break

        else:
            print("Option invalide. Veuillez essayer à nouveau.")

        sleep(2)  # Pause de 2 secondes pour rendre l'interface plus agréable