import droite as d

DEBUG = True

"""UNE CLASSE POUR OBTENIR UNE VAL D'APPARTENANCE A UN ENSEMBLE FLOU REPRESENTER PAR UN TRIANGLE """


class FuzzyTriangle():
    """le triangle se compose de deuc segement avec un 0<=y<=1 """

    def __init__(self, limite1, limite2):
        self.l1 = limite1
        self.l2 = limite2
        self.init_triangles(limite1, limite2)

    def calcul_droite(self, point1, point2):
        xa, ya = point1
        xb, yb = point2

        a = (yb - ya) / (xb - xa)

        if (DEBUG): print "a = ({}-{}) / ({}-{})".format(yb, ya, xb, xa)

        b = ya - (a * xa)

        return a, b

    def init_triangles(self, limite1, limite2):
        # calcul de la premiere droite
        milieu = (limite2 + limite1) / 2

        d1_a, d1_b = self.calcul_droite((limite1, 0.0), (milieu, 1.0))
        self.d1 = d.Droite(d1_a, d1_b)
        # calcul de la deuxieme droite
        d2_a, d2_b = self.calcul_droite((milieu, 1.0), (limite2, 0.0))
        self.d2 = d.Droite(d2_a, d2_b)

    def get_appartenance(self, x):

        milieu = (self.l1 + self.l2) / 2
        if (x == milieu):
            return 1.0
        if (x < milieu):
            return self.d1.getY(x)
        if (x < milieu):
            return self.d2.getY(x)
