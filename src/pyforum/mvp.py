# Importation des classes nécessaires
from time import sleep
from pyforum.bd import BD
from pyforum.commentaire import Commentaire
from pyforum.forum import Forum
from pyforum.publication import Publication
from pyforum.utilisateur import Utilisateur


def afficher_menu():
    """Affiche les options du menu."""
    print("\n---- Menu ----")
    print("1. Créer un utilisateur")
    print("2. Créer un forum")
    print("3. Créer une publication")
    print("4. Ajouter un commentaire à une publication")
    print("5. Joindre un forum")
    print("6. Quitter")


def main():

    bd1 = BD(utilisateurs = [], forums = [], publications = [], commentaires = [], utilisateurs_forums = [] )

    while True:
        afficher_menu()

        # Demander à l'utilisateur de choisir une option valide
        try:
            choix = int(input("Choisissez une option (1-6): "))
        except ValueError:
            print("Veuillez entrer une valeur valide")
            continue

        if choix == '1':
            # Créer un utilisateur
            print("\nCréation d'un utilisateur...")
            adresseEmail = input("Entrez votre adresse email")
            nomUtilisateur = input("Entrez le nom d'utilisateur: ")
            motDePasse = input("Entrez votre mot de passe")
            listeDeForums = []


            # Créer l'utilisateur
            utilisateur = Utilisateur(nomUtilisateur, adresseEmail, motDePasse, listeDeForums)

            # Sauvegarde l'utilisateur dans la base de données
            bd1.creer_utilisateur(utilisateur)


        elif choix == '2':
            # Créer un forum
            print("\nCréation d'un forum...")
            nomForum = input("Entrez le nom du forum")
            descriptionForum = input("Entrez une description du forum")
            listePublications = []
            nomUtilisateurForum = input("Entrez votre nom d'utilisateur")

            # Vérifie si l'utilisateur existe dans la base de données
            utilisateur_trouve = None
            for user in bd1.utilisateurs:
                if user.nomUtilisateur == nomUtilisateurForum:
                    utilisateur_trouve = user
                    break

            
            if utilisateur_trouve:

                # Crée le forum
                forum = Forum(nomForum, descriptionForum, listePublications)

                # Sauvegarde le forum dans la base de données bd1
                bd1.creer_forum(forum)

                # Ajoute le forum à la liste de forums de l'utilisateur
                utilisateur_trouve.listeDeForums.append(forum)

                print(f"Le forum {nomForum} a été créé avec succès et ajouté à votre liste de forums.")
            else:
                print("Nom d'utilisateur introuvable. Veuillez entrer un nom d'utilisateur valide ou vous créer un compte.")


        elif choix == '3':
            # Créer une publication
            print("\nCréation d'une publication...")
            titrePublication = input("Entrez le titre de la publication")
            contenuPublication = input("Entrez le contenu de la publication")
            nomUtilisateurPublication = input("Entrez votre nom d'utilisateur")
            nomForumPublication = input("Entrez le nom du forum dont vous souhaiter faire une publication")
            listeCommentaires = []
            auteurPublication = None
            votePublication = []
            nombreDeVotePublication = 0
            

            # Vérifie si l'utilisateur existe dans la base de données
            utilisateur_trouve = None
            for user in bd1.utilisateurs:
                if user.nomUtilisateur == nomUtilisateurPublication:
                    utilisateur_trouve = user
                    break

            # Vérifie si le forum existe dans la base de données
            forum_trouve = None
            for forum in bd1.forums:
                if forum.nomForum == nomForumPublication:
                    forum_trouve = forum
                    break

            if utilisateur_trouve and forum_trouve:
                # Vérifie si l'utilisateur est membre du forum
                if utilisateur_trouve not in forum_trouve.listeUtilisateurs:
                    print("Vous devez être membre de ce forum pour publier.")
                    continue

                # Ajoute l'utilisateur comme l'auteur de la publication
                auteurPublication = utilisateur_trouve

                # Crée la publication
                publication = Publication(titrePublication, contenuPublication, listeCommentaires, auteurPublication)

                # Sauvegarde la publication dans la base de données
                bd1.creer_publication(publication)

                # Ajoute la publication dans la liste de publication de l'auteur
                utilisateur_trouve.listeDePublications.append(publication)

                # Ajoute la publication au forum correspondant
                forum_trouve.listePublications.append(publication)

                print(f"La publication {titrePublication} a été créé avec succès!")
            else:
                print("Nom d'utilisateur ou forum introuvable. Veuillez entrer un forum ou nom d'utilisateur valide.")
                


        elif choix == '4':
            # Ajouter un commentaire
            print("\nAjouter un commentaire...")
            contenuCommentaire = input("Entrez le contenu du commentaire")
            nomUtilisateurCommentaire = input("Entrez votre nom d'utilisateur")
            nomForumCommentaire = input("Entrez le nom du forum dont vous souhaitez commenter")
            nomPublicationCommentaire = input("Entrez le titre de la publication dont vous souhaitez commenter")
            auteurCommentaire = None
            voteCommentaire = []
            nombreDeVoteCommentaire = 0


            # Vérifie si l'utilisateur existe dans la base de données
            utilisateur_trouve = None
            for user in bd1.utilisateurs:
                if user.nomUtilisateur == nomUtilisateurCommentaire:
                    utilisateur_trouve = user
                    break

            # Vérifie si le forum existe dans la base de données
            forum_trouve = None
            for forum in bd1.forums:
                if forum.nomForum == nomForumCommentaire:
                    forum_trouve = forum
                    break

            # Vérifie si la publication existe dans la base de données
            publication_trouve = None
            for publication in bd1.publications:
                if publication.titrePublication == nomPublicationCommentaire:
                    publication_trouve = publication
                    break

            if utilisateur_trouve and forum_trouve and publication_trouve:
                # Vérifie si l'utilisateur est membre du forum
                if utilisateur_trouve not in forum_trouve.listeUtilisateurs:
                    print("Vous devez être membre de ce forum pour publier.")
                    continue

                # Ajoute l'utilisateur comme étant l'auteur du commentaire
                auteurCommentaire = utilisateur_trouve

                # Crée le commentaire
                commentaire = Commentaire(contenuCommentaire, auteurCommentaire)

                # Sauvegarde le commentaire dans la base de données
                bd1.creer_commentaire(commentaire)

                # Ajoute le commentaire à la liste de commentaires de l'auteur
                utilisateur_trouve.listeDeCommentaires.append(commentaire)

                # Ajoute le commentaire à la publication correspondante
                publication_trouve.listeCommentaires.append(commentaire)

                print("Commentaire créé avec succès!")
            else:
                print("Utilisateur, forum ou publication introuvable. Veuillez entrer un forum, un nom d'utilisateur ou une publication valide.")



        elif choix == '5':
            # Joindre un forum
            print("\nJoindre un forum...")
            nomUtilisateurJoindreForum = input("Entrez votre nom d'utilisateur")
            nomForumJoindreForum = input("Entrez le nom du forum que vous souhaitez joindre")

            # Vérifie si l'utilisateur existe dans la base de données
            utilisateur_trouve = None
            for user in bd1.utilisateurs:
                if user.nomUtilisateur == nomUtilisateurJoindreForum:
                    utilisateur_trouve = user
                    break

            # Vérifie si le forum existe dans la base de données
            forum_trouve = None
            for forum in bd1.forums:
                if forum.nomForum == nomForumJoindreForum:
                    forum_trouve = forum
                    break

            if utilisateur_trouve and forum_trouve:
                # Ajoute l'utilisateur à la liste d'utilisateurs du forum correspondant
                forum_trouve.listeUtilisateurs.append(utilisateur_trouve)

                # Ajoute le forum correspondant à la liste de forum de l'utilisateur
                utilisateur_trouve.listeDeForums.append(forum_trouve)

                print("Vous avez rejoint le forum avec succès!")
            else:
                print("Nom d'utilisateur ou forum introuvable. Veuillez entrer un forum ou nom d'utilisateur valide.")


        elif choix == '6':
            # Quitter le programme
            print("\nMerci d'avoir utilisé PyForum. À bientôt!")
            break

        else:
            print("Option invalide. Veuillez essayer à nouveau.")

        sleep(2)  # Pause de 2 secondes pour rendre l'interface plus agréable