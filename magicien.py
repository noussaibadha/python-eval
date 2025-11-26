import random
from personnage import Personnage

class MagicienBlanc(Personnage):
    def __init__(self):
        frappes = [
            {"nom": "Lumière sacrée", "force": 15, "xp": 5},
            {"nom": "Explosion mystique", "force": 22, "xp": 8},
        ]
        super().__init__("Magicien blanc", frappes)
        self.tour = "joueur1"
        self._taux_esquive = 0.35

    def esquive(self):
        return random.random() < self._taux_esquive

    def choisir_frappe(self):
        return random.choice(self.frappes)
