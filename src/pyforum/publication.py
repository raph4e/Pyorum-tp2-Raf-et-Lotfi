from pyforum.bd import BD

class Publication():

    __id_count = 0

    def __init__(self, titrePublication, contenuPublication, listeCommentaires, auteurPublication, votePublication, nombreDeVotePublication, db: BD):
        self.titrePublication = titrePublication
        self.contenuPublication = contenuPublication
        self.listeCommentaires = listeCommentaires
        self.idPublication = Publication.__id_count
        Publication.__id_count += 1
        self.db = db
        self.auteurPublication = auteurPublication
        self.votePublication = votePublication
        self.nombreDeVotePublication = nombreDeVotePublication
        

    def __str__(self):
        return f"{self.titrePublication}, {self.contenuPublication}, {self.idPublication}"