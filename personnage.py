import random
from abc import ABC, abstractmethod

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"


class Personnage(ABC):
    def __init__(self, nom, frappes):
        self.__nom = None
        self.__vie = 100
        self.__frappes = None
        self.__experience = 0
        self.__degats = 0

        self.tour = None

        self.nom = nom
        self.frappes = frappes


    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Nom invalide")
        self.__nom = value

    @property
    def vie(self):
        return self.__vie

    @vie.setter
    def vie(self, value):
        if value <= 0:
            raise ValueError("Vie doit être positive")
        self.__vie = value

    @property
    def frappes(self):
        return self.__frappes

    @frappes.setter
    def frappes(self, value):
        if not isinstance(value, list) or not value:
            raise ValueError("Frappes doit être une liste")
        self.__frappes = value

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        if value < 0:
            raise ValueError("XP invalide")
        self.__experience = value

    @property
    def degats(self):
        return self.__degats

    @degats.setter
    def degats(self, value):
        if value < 0:
            raise ValueError("Dégats invalide")
        self.__degats = value


    def vie_restante(self):
        return max(self.vie - self.degats, 0)

    def frappe(self, cible, frappe):
        print(f"{CYAN}{self.nom}{RESET} utilise {YELLOW}{frappe['nom']}{RESET} ⚔️")

        if cible.esquive():
            print(f"{GREEN}{cible.nom} esquive ! 🛡️{RESET}\n")
            return

        cible.recoit_degats(self, frappe["force"])
        self.experience += frappe["xp"]

        print(f"{RED}Touché ! {frappe['force']} dégâts infligés.{RESET}🔥")
        print(f"➡️ Vie de {cible.nom} : {cible.vie_restante()} | XP : {self.experience}\n")

    def recoit_degats(self, adversaire, force):
        total = force + adversaire.experience
        self.degats += total

    @abstractmethod
    def esquive(self):
        pass

    @abstractmethod
    def choisir_frappe(self):
        pass