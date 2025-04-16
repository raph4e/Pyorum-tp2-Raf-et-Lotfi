from pyforum.bd import BD

class Publication():

    __id_count = 0

    def __init__(self, titrePublication, contenuPublication, listeCommentaires, dateCreation, identifiantAuteur, identifiantForumAuteur, db: BD):
        self.titrePublication = titrePublication
        self.contenuPublication = contenuPublication
        self.listeCommentaires = listeCommentaires
        self.dateCreation = dateCreation
        self.identifiantAuteur = identifiantAuteur
        self.identifiantForumAuteur = identifiantForumAuteur
        self.idPublication = Publication.__id_count
        Publication.__id_count += 1
        self.db = db

        

    def __str__(self):
        return f"{self.titrePublication}, {self.contenuPublication}, {self.idPublication}"