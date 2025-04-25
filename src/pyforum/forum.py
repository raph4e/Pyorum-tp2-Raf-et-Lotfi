

class Forum():

    # Initialisation de l'instance forum
    def __init__(self, new_id_forum, nomForum, descriptionForum, listePublications):
        self.nomForum = nomForum
        self.descriptionForum = descriptionForum
        self.listePublications = listePublications
        self.new_id_forum = new_id_forum
        
        
    # Fonction qui affiche les informations du forum
    def __str__(self):
        return f"{self.nomForum}, {self.descriptionForum}, {self.new_id_forum}"

   