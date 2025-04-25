from pyforum.utilisateur import Utilisateur
from pyforum.forum import Forum
from pyforum.commentaire import Commentaire
from pyforum.publication import Publication



class BD:
    def __init__(self):
        self.utilisateurs: list[Utilisateur] = []
        self.forums: list[Forum] = []
        self.publications: list[Publication] = []
        self.commentaires: list[Commentaire] = []
        self.utilisateurs_forums = {} 
        print("Base de données initialisée.")

    # Fonction pour créer un utilisateur
    def creer_utilisateur(self, nomUtilisateur: str, adresseEmail: str, motDePasse: str, listeDeForums: list) -> Utilisateur:
        # Vérifier si l'utilisateur existe déjà
        if nomUtilisateur in [u.nomUtilisateur for u in self.utilisateurs]:
            print(f"[Simulé] L'utilisateur {nomUtilisateur} existe déjà.")
            return

        # Lire le dernier ID utilisateur depuis le fichier CSV
        try:
            with open("src/pyforum/Fichiers_CSV/Utilisateur.csv", "r") as f:
                lignes = f.readlines()
                dernier_id = 0  # Valeur par défaut si le fichier est vide 
                for ligne in lignes[1:]:  # Ignorer l'en-tête
                    try:
                        # Tenter de convertir le premier élément de la ligne en entier
                        dernier_id = int(ligne.split(",")[0])
                    except ValueError:
                        continue
        except FileNotFoundError:
            # Si le fichier n'existe pas encore
            dernier_id = 0

        # Créer un nouvel identifiant pour l'utilisateur
        new_id_utilisateur = dernier_id + 1

        # Instancier un nouvel utilisateur et l'ajouter à la liste
        u = Utilisateur(new_id_utilisateur, nomUtilisateur, adresseEmail, motDePasse, listeDeForums)
        self.utilisateurs.append(u)
        print(f"[Simulé] Sauvegarde de l'utilisateur: {u}")

        # Ajouter l'utilisateur au fichier CSV
        with open("src/pyforum/Fichiers_CSV/Utilisateur.csv", "a") as f:
            # Écrire les données dans l'ordre des colonnes
            f.write(f"{u.new_id_utilisateur},{u.nomUtilisateur},{u.adresseEmail},{u.motDePasse},{'|'.join(u.listeDeForums)}\n")

        # Retourner l'utilisateur créé
        return u
    
    # Fonction pour obtenir une instance utilisateur à partir de son nom
    def obtenir_utilisateur_par_nom(self, nom_utilisateur: str):
        for u in self.utilisateurs:
            if u.nomUtilisateur == nom_utilisateur:
                return u

    # Fonction pour créer un forum
    def creer_forum(self, nomForum, descriptionForum, listePublications, utilisateur_trouve: Utilisateur):
        # Vérifier si le forum existe déjà
        if nomForum in [f.nomForum for f in self.forums]:
            print(f"[Simulé] Le forum {nomForum} existe déjà.")
            return

        # Lire le dernier ID forum depuis le fichier CSV
        try:
            with open("src/pyforum/Fichiers_CSV/Forum.csv", "r") as f:
                lignes = f.readlines()
                dernier_id = 0  # Valeur par défaut si le fichier est vide 
                for ligne in lignes[1:]:  # Ignorer l'en-tête
                    try:
                        dernier_id = int(ligne.split(",")[0])
                    except ValueError:
                        continue
        except FileNotFoundError:
            dernier_id = 0  # Si le fichier n'existe pas encore

        # Créer un nouvel identifiant pour le forum
        new_id_forum = dernier_id + 1

        # Instancier un nouveau forum et l'ajouter à la liste
        fo = Forum(new_id_forum, nomForum, descriptionForum, listePublications)
        self.forums.append(fo)
        print(f"[Simulé] Sauvegarde du forum: {fo}")

        # Ajouter le forum au fichier CSV
        with open("src/pyforum/Fichiers_CSV/Forum.csv", "a") as f:
            f.write(f"{fo.new_id_forum},{fo.nomForum},{fo.descriptionForum},{'|'.join(fo.listePublications)}\n")
        
        # Ajoute le forum à la liste de forums de l'utilisateur
        utilisateur_trouve.listeDeForums.append(fo.nomForum)
        self.mettre_a_jour_utilisateur_csv(utilisateur_trouve)

        # Retourner le forum créé
        return fo
    
    # Fonction pour obtenir une instance forum à partir de son nom
    def obtenir_forum_par_nom(self, nom_forum: str):
        for f in self.forums:
            if f.nomForum == nom_forum:
                return f

    # Fonction pour créer une publication
    def creer_publication(self, titrePublication, contenuPublication, dateCreation, identifiantAuteur, identifiantForumAuteur, listeCommentaires, forum_trouve: Forum):
        # Vérifier si la publication existe déjà
        if titrePublication in [p.titrePublication for p in self.publications]:
            print(f"[Simulé] La publication {titrePublication} existe déjà.")
            return

        # Lire le dernier ID publication depuis le fichier CSV
        try:
            with open("src/pyforum/Fichiers_CSV/Publication.csv", "r") as f:
                lignes = f.readlines()
                dernier_id = 0  # Valeur par défaut si le fichier est vide 
                for ligne in lignes[1:]:  # Ignorer l'en-tête
                    try:
                        dernier_id = int(ligne.split(",")[0])
                    except ValueError:
                        continue
        except FileNotFoundError:
            dernier_id = 0  # Si le fichier n'existe pas encore

        # Créer un nouvel identifiant pour la publication
        new_id_publication = dernier_id + 1

        # Instancier une nouvelle publication et l'ajouter à la liste
        p = Publication(new_id_publication, titrePublication, contenuPublication, dateCreation, identifiantAuteur, identifiantForumAuteur, listeCommentaires)
        self.publications.append(p)
        print(f"[Simulé] Sauvegarde de la publication: {p}")

        # Ajouter la publication au fichier CSV
        with open("src/pyforum/Fichiers_CSV/Publication.csv", "a") as f:
            f.write(f"{p.new_id_publication},{p.titrePublication},{p.contenuPublication},{p.dateCreation},{p.identifiantAuteur},{p.identifiantForumAuteur},{'|'.join(p.listeCommentaires)}\n")

        # Ajoute la publication à la liste de publication du forum
        forum_trouve.listePublications.append(p.titrePublication)
        self.mettre_a_jour_forum_csv(forum_trouve)

        # Retourner la publication créée
        return p
    
    # Fonction pour obtenir une instance publication à partir de son titre 
    def obtenir_publication_par_titre(self, titre_publication):
        for p in self.publications:
            if p.titrePublication == titre_publication:
                return p

    # Fonction pour créer un commentaire
    def creer_commentaire(self, contenuCommentaire, identifiantAuteur, identifiantPublication, publication_trouve: Publication):
        # Lire le dernier ID commentaire depuis le fichier CSV
        try:
            with open("src/pyforum/Fichiers_CSV/Commentaire.csv", "r") as f:
                lignes = f.readlines()
                dernier_id = 0  # Valeur par défaut si le fichier est vide 
                for ligne in lignes[1:]:  # Ignorer l'en-tête
                    try:
                        dernier_id = int(ligne.split(",")[0])
                    except ValueError:
                        continue
        except FileNotFoundError:
            dernier_id = 0  # Si le fichier n'existe pas encore

        # Créer un nouvel identifiant pour le commentaire
        new_id_commentaire = dernier_id + 1

        # Instancier un nouveau commentaire et l'ajouter à la liste
        c = Commentaire(new_id_commentaire, contenuCommentaire, identifiantAuteur, identifiantPublication)
        self.commentaires.append(c)
        print(f"[Simulé] Sauvegarde du commentaire: {c}")

        # Ajouter le commentaire au fichier CSV
        with open("src/pyforum/Fichiers_CSV/Commentaire.csv", "a") as f:
            f.write(f"{c.new_id_commentaire},{c.contenuCommentaire},{c.identifiantAuteur},{c.identifiantPublication}\n")

        # Ajoute le commentaire à la liste de commentaires de la publication
        publication_trouve.listeCommentaires.append(c.contenuCommentaire)
        self.mettre_a_jour_publication_csv(publication_trouve)
        
        # Retourner le commentaire créé
        return c
    
    # Fonction pour joindre un forum
    def joindre_forum(self, utilisateur_trouve: Utilisateur, forum_trouve: Forum):

        # Ajoute le forum à la liste de forums de l'utilisateur
        utilisateur_trouve.listeDeForums.append(forum_trouve.nomForum)
        self.mettre_a_jour_utilisateur_csv(utilisateur_trouve)

    
    # Met à jour les informations d'un utilisateur dans le fichier CSV
    def mettre_a_jour_utilisateur_csv(self, utilisateur: Utilisateur):
        try:
            with open("src/pyforum/Fichiers_CSV/Utilisateur.csv", "r") as f:
                lignes = f.readlines()

            # Réécrire le fichier avec les informations mises à jour
            with open("src/pyforum/Fichiers_CSV/Utilisateur.csv", "w") as f:
                for ligne in lignes:
                    # Vérifier si c'est l'utilisateur à mettre à jour
                    if ligne.startswith(f"{utilisateur.new_id_utilisateur},"):
                        # Mettre à jour la ligne avec les nouvelles informations
                        f.write(f"{utilisateur.new_id_utilisateur},{utilisateur.nomUtilisateur},{utilisateur.adresseEmail},{utilisateur.motDePasse},{'|'.join(utilisateur.listeDeForums)}\n")
                    else:
                        # Réécrire les autres lignes sans modification
                        f.write(ligne)
        except FileNotFoundError:
            print("Le fichier Utilisateur.csv est introuvable.")


    # Met à jour les informations d'un forum dans le fichier CSV
    def mettre_a_jour_forum_csv(self, forum: Forum):
        try:
            with open("src/pyforum/Fichiers_CSV/Forum.csv", "r") as f:
                lignes = f.readlines()

            # Réécrire le fichier avec les informations mises à jour
            with open("src/pyforum/Fichiers_CSV/Forum.csv", "w") as f:
                for ligne in lignes:
                    # Vérifier si c'est le forum à mettre à jour
                    if ligne.startswith(f"{forum.new_id_forum},"):
                        # Mettre à jour la ligne avec les nouvelles informations
                        f.write(f"{forum.new_id_forum},{forum.nomForum},{forum.descriptionForum},{'|'.join(forum.listePublications)}\n")
                    else:
                        # Réécrire les autres lignes sans modification
                        f.write(ligne)
        except FileNotFoundError:
            print("Le fichier Forum.csv est introuvable.")

    
    # Met à jour les informations d'une publication dans le fichier CSV
    def mettre_a_jour_publication_csv(self, publication: Publication):
        try:
            with open("src/pyforum/Fichiers_CSV/Publication.csv", "r") as f:
                lignes = f.readlines()

            # Réécrire le fichier avec les informations mises à jour
            with open("src/pyforum/Fichiers_CSV/Publication.csv", "w") as f:
                for ligne in lignes:
                    # Vérifier si c'est la publication à mettre à jour
                    if ligne.startswith(f"{publication.new_id_publication},"):
                        # Mettre à jour la ligne avec les nouvelles informations
                        f.write(f"{publication.new_id_publication},{publication.titrePublication},{publication.contenuPublication},{publication.dateCreation},{publication.identifiantAuteur},{publication.identifiantForumAuteur},{'|'.join(publication.listeCommentaires)}\n")
                    else:
                        # Réécrire les autres lignes sans modification
                        f.write(ligne)
        except FileNotFoundError:
            print("Le fichier Publication.csv est introuvable.")





