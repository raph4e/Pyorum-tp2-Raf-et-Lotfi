from pyforum.bd import BD

class Forum():

    __id_count = 0

    def __init__(self, nomForum, descriptionForum, listePublications, db: BD):
        self.nomForum = nomForum
        self.descriptionForum = descriptionForum
        self.listePublications = listePublications
        self.idForum = Forum.__id_count
        Forum.__id_count += 1
        self.db = db
        

    def __str__(self):
        return f"{self.nomForum}, {self.descriptionForum}, {self.idForum}"

   