from pyforum.bd import BD

class Utilisateur():

    __id_count = 0

    def __str__(self):
        return f"{self.nomUtilisateur}, {self.adresseEmail}, {self.idUtilisateur}"

    def __init__(self, nomUtilisateur, adresseEmail, motDePasse, listeDeForums, db: BD):
        self.nomUtilisateur = nomUtilisateur
        self.adresseEmail = adresseEmail
        self.motDePasse = motDePasse
        self.listeDeForums = listeDeForums
        self.db = db
        self.idUtilisateur = Utilisateur.__id_count
        Utilisateur.__id_count += 1
