from pyforum.bd import BD

class Commentaire(BD):
        
    __id_count = 0

    def __init__(self, contenuCommentaire, auteurCommentaire, voteCommentaire, nombreDeVoteCommentaire, db: BD):
        self.contenuCommentaire = contenuCommentaire
        self.idCommentaire = Commentaire.__id_count
        Commentaire.__id_count += 1
        self.db = db
        self.auteurCommentaire = auteurCommentaire
        self.voteCommentaire = voteCommentaire
        self.nombreDeVoteCommentaire = nombreDeVoteCommentaire
        

    def __str__(self):
        return f"{self.contenuCommentaire}, {self.idCommentaire}"