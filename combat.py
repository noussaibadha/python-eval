from magicien import MagicienBlanc
from roisorcier import RoiSorcier

from personnage import (
    BOLD, BLUE, GREEN, RED, YELLOW, RESET, MAGENTA
)


def lancer_combat():
    magicien = MagicienBlanc()
    roi = RoiSorcier()

    print(f"{BOLD}{BLUE}=== MAGICIEN BLANC VS ROI SORCIER === ⚡{RESET}\n")

    attaquant = magicien
    défenseur = roi
    tour = 1

    while magicien.vie_restante() > 0 and roi.vie_restante() > 0:
        print(f"{BOLD}{MAGENTA}----- Tour {tour} -----{RESET}")
        frappe = attaquant.choisir_frappe()
        attaquant.frappe(défenseur, frappe)

        if défenseur.vie_restante() <= 0:
            break

        attaquant, défenseur = défenseur, attaquant
        tour += 1

    if magicien.vie_restante() <= 0:
        print(f"{RED}Le Roi sorcier gagne ! 💀{RESET}")
    else:
        print(f"{GREEN}Le Magicien blanc remporte la victoire ! 🏆{RESET}")
