class FichierJoint:
    def __init__(self, nom_fichier, type_fichier, taille):
        """
        Initialise un fichier joint.
        :param nom_fichier: Nom du fichier.
        :param type_fichier: Type du fichier (par exemple, 'PDF', 'JPEG').
        :param taille: Taille du fichier en Ko.
        """
        self.nom_fichier = nom_fichier
        self.type_fichier = type_fichier
        self.taille = taille


class Email:
    def __init__(self, titre, texte, expediteur, destination):
        """
        Initialise un email.
        :param titre: Titre de l'email.
        :param texte: Contenu de l'email.
        :param expediteur: Adresse email de l'expéditeur.
        :param destination: Adresse email du destinataire.
        """
        self.titre = titre
        self.texte = texte
        self.expediteur = expediteur
        self.destination = destination
        self.fichiers_joints = []

    def ajouter_fichier_joint(self, fichier):
        """
        Ajoute un fichier joint à l'email.
        :param fichier: Instance de la classe FichierJoint.
        """
        self.fichiers_joints.append(fichier)

    def afficher_details(self):
        """
        Affiche les détails de l'email.
        """
        print(f"Titre: {self.titre}")
        print(f"Expéditeur: {self.expediteur}")
        print(f"Destinataire: {self.destination}")
        print(f"Texte: {self.texte}")
        print("Fichiers joints:")
        for fichier in self.fichiers_joints:
            print(f"- {fichier.nom_fichier} ({fichier.type_fichier}, {fichier.taille} Ko)")
