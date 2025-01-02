class Habitat:
    def __init__(self, nom):
        """
        Initialise un habitat.
        :param nom: Nom de l'habitat.
        """
        self.nom = nom


class Animal:
    def __init__(self, habitat):
        """
        Initialise un animal.
        :param habitat: Instance de la classe Habitat.
        """
        self.habitat = habitat
        self.tete = None
        self.corps = None
        self.membres = []

    def manger(self):
        """
        Méthode à redéfinir par les classes filles.
        """
        raise NotImplementedError("Cette méthode doit être redéfinie dans une classe enfant")


class Herbivore(Animal):
    def manger(self):
        """
        Spécifie le comportement de manger pour un herbivore.
        """
        print("Cet herbivore mange des plantes.")


class Carnivore(Animal):
    def manger(self):
        """
        Spécifie le comportement de manger pour un carnivore.
        """
        print("Ce carnivore mange de la viande.")


class Tete:
    def __init__(self, taille):
        """
        Initialise une tête.
        :param taille: Taille de la tête.
        """
        self.taille = taille


class Corps:
    def __init__(self, taille, poids):
        """
        Initialise un corps.
        :param taille: Taille du corps.
        :param poids: Poids du corps.
        """
        self.taille = taille
        self.poids = poids


class Membres:
    def __init__(self, nombre):
        """
        Initialise les membres.
        :param nombre: Nombre de membres.
        """
        self.nombre = nombre
