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

        # Créer un nouvel identifiant pour l'utilisateur
        new_id_utilisateur = max([u.new_id_utilisateur for u in self.utilisateurs], default=0) + 1

        # Instancier un nouvel utilisateur et l'ajouter à la liste
        u = Utilisateur(new_id_utilisateur, nomUtilisateur, adresseEmail, motDePasse, listeDeForums)
        self.utilisateurs.append(u)
        print(f"[Simulé] Sauvegarde de l'utilisateur: {u}")

        # Ajouter l'utilisateur au fichier csv Utilisateur.csv
        with open("Utilisateur.csv", "a") as f:
            f.write(f"{u.new_id_utilisateur},{u.nomUtilisateur},{u.adresseEmail},{u.motDePasse},{u.listeDeForums}\n")
            
        # Retourner l'utilisateur créé
        return u
    
    # Fonction pour obtenir une instance utilisateur à partir de son nom
    def obtenir_utilisateur_par_nom(self, nom_utilisateur: str):
        for u in self.utilisateurs:
            if u.nomUtilisateur == nom_utilisateur:
                return u

    # Fonction pour créer un forum
    def creer_forum(self, nomForum, descriptionForum, listePublications):

        # Vérifier si le forum existe déjà
        if nomForum in [f.nomForum for f in self.forums]:
            print(f"[Simulé] Le forum {nomForum} existe déjà.")
            return
        
        # Créer un nouvel identifiant pour le forum
        new_id_forum = max([f.new_id_forum for f in self.forums], default=0) + 1

        # Instancier un nouveau forum et l'ajouter à la liste
        f = Forum(new_id_forum, nomForum, descriptionForum, listePublications)
        self.forums.append(f)
        print(f"[Simulé] Sauvegarde du forum: {f}")

        # Ajouter le forum au fichier csv Forum.csv
        with open("Forum.csv", "a") as f:
            f.write(f"{f.new_id_forum},{f.nomForum},{f.descriptionForum},{f.listePublications}\n")

        # Retourner le forum créé
        return f
    
    # Fonction pour obtenir une instance forum à partir de son nom
    def obtenir_forum_par_nom(self, nom_forum: str):
        for f in self.forums:
            if f.nomForum == nom_forum:
                return f

    # Fonction pour créer une publication
    def creer_publication(self, titrePublication, contenuPublication, listeCommentaires, dateCreation, identifiantAuteur, identifiantForumAuteur):

        # Vérifier si la publication existe déjà
        if titrePublication in [p.titrePublication for p in self.publications]:
            print(f"[Simulé] Le forum {titrePublication} existe déjà.")
            return 
        
        # Créer un nouvel identifiant pour la publication
        new_id_publication = max([p.new_id_publication for p in self.publications], default=0) + 1

        # Instancier une nouvelle publication et l'ajouter à la liste
        p = Publication(new_id_publication, titrePublication, contenuPublication, listeCommentaires, dateCreation, identifiantAuteur, identifiantForumAuteur)
        self.publications.append(p)
        print(f"[Simulé] Sauvegarde du forum: {p}")
        # Ajouter la publication au fichier csv Publication.csv
        with open("Publication.csv", "a") as f:
            f.write(f"{p.new_id_publication},{p.titrePublication},{p.contenuPublication},{p.listeCommentaires},{p.dateCreation},{p.identifiantAuteur},{p.identifiantForumAuteur}\n")

        # Retourner la publication créé
        return p
    
    # Fonction pour obtenir une instance publication à partir de son titre 
    def obtenir_publication_par_titre(self, titre_publication):
        for p in self.publications:
            if p.titrePublication == titre_publication:
                return p

    # Fonction pour créer un commentaire
    def creer_commentaire(self, contenuCommentaire, identifiantAuteur, identifiantPublication):
        
        # Créer un nouvel identifiant pour la publication
        new_id_commentaire = max([c.new_id_commentaire for c in self.commentaires], default=0) + 1

        # Instancier une nouvelle publication et l'ajouter à la liste
        c = Commentaire(new_id_commentaire, contenuCommentaire, identifiantAuteur, identifiantPublication)
        self.publications.append(c)
        print(f"[Simulé] Sauvegarde du forum: {c}")
        # Ajouter le commentaire au fichier csv Commentaire.csv
        with open("Commentaire.csv", "a") as f:
            f.write(f"{c.new_id_commentaire},{c.contenuCommentaire},{c.identifiantAuteur},{c.identifiantPublication}\n")

        # Retourner la publication créé
        return c



