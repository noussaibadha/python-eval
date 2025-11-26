import random
from personnage import Personnage

class RoiSorcier(Personnage):
    def __init__(self):
        frappes = [
            {"nom": "Lame maudite", "force": 18, "xp": 4},
            {"nom": "Ombre écrasante", "force": 24, "xp": 7},
        ]
        super().__init__("Roi sorcier", frappes)
        self.tour = "joueur2"
        self._taux_esquive = 0.25

    def esquive(self):
        return random.random() < self._taux_esquive

    def choisir_frappe(self):
        return random.choice(self.frappes)
