from fuzzyTriangle import FuzzyTriangle

DEBUG = False

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
        if DEBUG:
            print "init :"
            print str(self.name)
            print str(self.code)
            print str(self.limite_gauche) + " , " + str(self.limite_droite)

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
        if DEBUG: print "group appartenance x = " + str(x)
        return self.triangle.get_appartenance(x)
