

class Publication():

    # Initialisation de l'instance publication
    def __init__(self, new_id_publication, titrePublication, contenuPublication, dateCreation, identifiantAuteur, identifiantForumAuteur, listeCommentaires):
        self.titrePublication = titrePublication
        self.contenuPublication = contenuPublication
        self.listeCommentaires = listeCommentaires
        self.dateCreation = dateCreation
        self.identifiantAuteur = identifiantAuteur
        self.identifiantForumAuteur = identifiantForumAuteur
        self.new_id_publication = new_id_publication

        
    # Fonction qui affiche les informations de la publication
    def __str__(self):
        return f"{self.titrePublication}, {self.contenuPublication}, {self.new_id_publication}"