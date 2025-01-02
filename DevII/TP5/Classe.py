class DossierPersonnel:
    """
    Représente les informations personnelles d'une personne.
    """
    def __init__(self, etat_civil: str, coordonnees: str):
        self.etat_civil = etat_civil
        self.coordonnees = coordonnees


class Personne:
    """
    Classe parent pour représenter une personne avec un dossier personnel.
    """
    def __init__(self, nom: str, prenom: str, dossier: DossierPersonnel):
        self.nom = nom
        self.prenom = prenom
        self.dossier = dossier


class Professeur(Personne):
    """
    Représente un professeur avec une matière spécifique.
    """
    def __init__(self, nom: str, prenom: str, matiere: str, dossier: DossierPersonnel):
        super().__init__(nom, prenom, dossier)
        self.matiere = matiere


class Eleve(Personne):
    """
    Représente un élève avec un niveau d'étude spécifique.
    """
    def __init__(self, nom: str, prenom: str, niveau_etude: str, dossier: DossierPersonnel):
        super().__init__(nom, prenom, dossier)
        self.niveau_etude = niveau_etude


class Classe:
    """
    Représente une classe composée de 1 professeur et de 0 à 30 élèves.
    """
    def __init__(self):
        self.professeur = None
        self.eleves = []

    def ajouter_professeur(self, professeur: Professeur):
        """
        Ajoute un professeur à la classe.
        Précondition : Aucun autre professeur ne doit être déjà associé à la classe.
        """
        if self.professeur is not None:
            raise ValueError("Un professeur est déjà assigné à cette classe.")
        self.professeur = professeur

    def ajouter_eleve(self, eleve: Eleve):
        """
        Ajoute un élève à la classe.
        Précondition : Le nombre d'élèves ne doit pas dépasser 30.
        """
        if len(self.eleves) >= 30:
            raise ValueError("La classe ne peut pas contenir plus de 30 élèves.")
        self.eleves.append(eleve)
