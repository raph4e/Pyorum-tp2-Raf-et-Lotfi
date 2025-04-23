

class Commentaire():

    # Initialisation de l'instance commentaire     
    def __init__(self, contenuCommentaire, identifiantAuteur, identifiantPublication, new_id_commentaire):
        self.contenuCommentaire = contenuCommentaire
        self.identifiantAuteur = identifiantAuteur
        self.new_id_commentaire = new_id_commentaire
        self.identifiantPublication = identifiantPublication
        

        
    # Fonction qui affiche les informations du commentaire
    def __str__(self):
        return f"{self.contenuCommentaire}, {self.new_id_commentaire}, {self.identifiantPublication}"