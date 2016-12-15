from group import group


class Rule():
    def __init__(self):
        self.PM = group("PM", 2, 30.0, 90.0)
        self.PS = group("PS", 1, 0.0, 60.0)
        self.ZR = group("ZR", 0, -30.0, 30.0)
        self.NS = group("NS", -1, -60.0, 0.0)
        self.NM = group("NM", -2, -90.0, -30.0)
        self.list_groups = []
        self.list_groups.append(self.PM)
        self.list_groups.append(self.PS)
        self.list_groups.append(self.ZR)
        self.list_groups.append(self.NS)
        self.list_groups.append(self.NM)

        # tableau 2D pour representer les regles : axes des x la pos angulaire
        # axes des y la v angulaire
        self.rule_table = [
            [-5, -5, self.NS, -5, -5],
            [-5, self.NS, self.ZR, self.ZR, -5],
            [self.NM, -5, self.ZR, -5, self.PM],
            [-5, self.ZR, self.ZR, self.PS, -5],
            [-5, -5, self.PS, -5, -5]]

        self.fuzzy_set_limit_angle = [(-90.0, -30.0),
                                      (-60.0, 0.0),
                                      (-30.0, 30.0),
                                      (0.0, 60.0),
                                      (30.0, 90.0)]
        self.angle_groups = []

        self.fuzzy_set_limit_speed = [(-90.0, -30.0),
                                      (-60.0, 0.0),
                                      (-30.0, 30.0),
                                      (0.0, 60.0),
                                      (30.0, 90.0)]
        self.speed_groups = []

    def activated_rule_pos(self, angle):
        # dico qui contient les resultat sous forme
        # code : degre d'appartenace
        res = {}
        for g in self.list_groups:
            if g.is_in(g):
                res[g.name] = g.appartenance(angle)
        return res

    def activated_rule_vitesse(self, vitesse):
        res = {}
        for g in self.list_groups:
            if g.is_in(g):
                res[g.name] = g.appartenance(vitesse)
        return res

    # fonction qui retourne la force selon l'angle
    def apply_rule(self, x, y):

        active_x = self.activated_rule_pos(x)
        active_y = self.activated_rule_vitesse(y)
