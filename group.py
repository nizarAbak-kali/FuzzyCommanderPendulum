from fuzzyTriangle import FuzzyTriangle

"""
CLASS REPRESENTING LES GROUPES
"""


class group:
    def __init__(self, n, c=0, lg=0, ld=0):
        self.name = n
        self.code = c
        self.limite_gauche = lg
        self.limite_droite = ld
        self.triangle = FuzzyTriangle(self.limite_gauche, self.limite_droite)

    def limits(self):
        return self.limite_gauche, self.limite_droite

    def name(self):
        return self.name

    def code(self):
        return self.code

    def is_in(self, x):
        if x <= self.limite_droite and x >= self.limite_gauche:
            return True
        else:
            return False

    """degre d'appartenace au groupe"""

    def appartenance(self, x):
        return self.triangle.get_appartenance(x)
