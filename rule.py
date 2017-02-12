from group import group

DEBUG = True

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
        if DEBUG: print "activated rule pos : " + str(angle)
        for g in self.list_groups:
            if g.is_in(angle):
                res[g.name] = g.appartenance(angle)
        return res

    def activated_rule_vitesse(self, vitesse):
        res = {}
        if DEBUG: print "activated rule vitesse : " + str(vitesse)
        for g in self.list_groups:
            if g.is_in(vitesse):
                res[g.name] = g.appartenance(vitesse)
        return res

    def return_coord(self, active):
        coord_x = []
        if (active.has_key("NM")): coord_x.append(0)
        if (active.has_key("NS")): coord_x.append(1)
        if (active.has_key("ZR")): coord_x.append(2)
        if (active.has_key("PS")): coord_x.append(3)
        if (active.has_key("PM")): coord_x.append(4)
        return coord_x

    def return_code(self, coord):

        if (coord == 0): return "NM"
        if (coord == 1): return "NS"
        if (coord == 2): return "ZR"
        if (coord == 3): return "PS"
        if (coord == 4): return "PM"

    # fonction qui retourne la force selon l'angle
    def apply_rule(self, x, y):

        active_x = self.activated_rule_pos(x)
        active_y = self.activated_rule_vitesse(y)

        if DEBUG: print 'apply RULE'
        if DEBUG: print "active angle rule :" + str(active_x)
        if DEBUG: print "active vitesse rule :" + str(active_y)

        coord_x = self.return_coord(active_x)
        coord_y = self.return_coord(active_y)

        if DEBUG: print "coord_x : " + str(coord_x)
        if DEBUG: print "coord_y : " + str(coord_y)

        rule_activated = []
        for j in coord_y:
            for i in coord_x:
                if (self.rule_table[j][i] != -5):
                    val = self.rule_table[j][i]
                    if DEBUG: print "regle active : " + val.name
                    rule_activated.append(val)

        # on retire les degres d'appartenance nul
        for i in rule_activated:
            if i == 0.0:
                rule_activated.remove(i)

        mini = min(rule_activated)
        if DEBUG: print "ET entre les different degrees"

        # ou entre les differente val
