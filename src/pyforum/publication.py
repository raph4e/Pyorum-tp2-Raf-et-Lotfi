from pyforum.bd import BD

class Publication():

    # Initialisation de l'instance publication
    def __init__(self, titrePublication, contenuPublication, listeCommentaires, dateCreation, identifiantAuteur, identifiantForumAuteur, new_id_publication, db: BD):
        self.titrePublication = titrePublication
        self.contenuPublication = contenuPublication
        self.listeCommentaires = listeCommentaires
        self.dateCreation = dateCreation
        self.identifiantAuteur = identifiantAuteur
        self.identifiantForumAuteur = identifiantForumAuteur
        self.new_id_publication = new_id_publication
        self.db = db

        
    # Fonction qui affiche les informations de la publication
    def __str__(self):
        return f"{self.titrePublication}, {self.contenuPublication}, {self.new_id_publication}"