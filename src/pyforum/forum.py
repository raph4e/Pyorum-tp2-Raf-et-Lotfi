

class Forum():

    # Initialisation de l'instance forum
    def __init__(self, nomForum, descriptionForum, listePublications, new_id_forum,):
        self.nomForum = nomForum
        self.descriptionForum = descriptionForum
        self.listePublications = listePublications
        self.new_id_forum = new_id_forum
        
        
    # Fonction qui affiche les informations du forum
    def __str__(self):
        return f"{self.nomForum}, {self.descriptionForum}, {self.new_id_forum}"

   