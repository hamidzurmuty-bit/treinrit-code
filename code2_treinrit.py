
def standaardprijs(afstand_km):
    """
    Berekent de standaardprijs van een treinrit.
    - Tot en met 50 km: €0.80 per km
    - Meer dan 50 km: €15 + €0.60 per km
    - Negatieve afstand = 0 km
    """
    if afstand_km < 0:
        afstand_km = 0

    if afstand_km > 50:
        prijs = 15 + 0.60 * afstand_km
    else:
        prijs = 0.80 * afstand_km
    return prijs


def ritprijs(leeftijd, weekendrit, afstand_km):
    """
    Berekent de uiteindelijke ritprijs met korting.
    - Kinderen (<12) en ouderen (≥65):
        * Doordeweeks: 30% korting
        * Weekend: 35% korting
    - Overige leeftijden:
        * Doordeweeks: geen korting
        * Weekend: 40% korting
    """
    basisprijs = standaardprijs(afstand_km)

    korting = 0
    if leeftijd < 12 or leeftijd >= 65:
        korting = 0.35 if weekendrit else 0.30
    else:
        korting = 0.40 if weekendrit else 0.00

    eindprijs = basisprijs * (1 - korting)
    return round(eindprijs, 2)
