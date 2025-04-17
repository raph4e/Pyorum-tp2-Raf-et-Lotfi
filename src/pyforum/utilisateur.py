from pyforum.bd import BD


class Utilisateur():

    # Initialisation de l'instance utilisateur
    def __init__(self, nomUtilisateur, adresseEmail, motDePasse, listeDeForums, new_id_utilisateur, db: BD):
        self.nomUtilisateur = nomUtilisateur
        self.adresseEmail = adresseEmail
        self.motDePasse = motDePasse
        self.listeDeForums = listeDeForums
        self.db = db
        self.new_id_utilisateur = new_id_utilisateur

    # Fonction qui affiche les informations de l'utilisateur
    def __str__(self):
        return f"{self.nomUtilisateur}, {self.adresseEmail}, {self.new_id_utilisateur}"
