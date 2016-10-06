# coding=utf-8
import csv

import fuzzyTriangle as fzt
import pendule as pd

"""
    Principe de l'evaluation :
        - en binome
        - programmation d'un systeme de controle floue pour un pendule inverse
        - ENTRES : - angle de la tige par rapport verticale
                   - vitesse angulaire (calculé)
"""

PM = 2
PS = 1
ZR = 0
NS = -1
NM = -2

rule_table = [[-5, -5, NS, -5, -5],
              [-5, NS, ZR, ZR, -5],
              [NM, -5, ZR, -5, PM],
              [-5, ZR, ZR, PS, -5],
              [-5, -5, PS, -5, -5]]

dico_rule_angle = {NM: (-90.0, -30.0), NS: (-60.0, 0.0), ZR: (-30.0, 30.0), PS: (0.0, 60.0), PM: (30.0, 90.0)}
fuzzy_set_limit_angle = [(-90.0, -30.0), (-60.0, 0.0), (-30.0, 30.0), (0.0, 60.0), (30.0, 90.0)]
angle_groups = []

# demander au prof
dico_rule_speed = {NM: (-90.0, -30.0), NS: (-60.0, 0.0), ZR: (-30.0, 30.0), PS: (0.0, 60.0), PM: (30.0, 90.0)}
fuzzy_set_limit_speed = [(-90.0, -30.0), (-60.0, 0.0), (-30.0, 30.0), (0.0, 60.0), (30.0, 90.0)]
speed_groups = []

la = []
lv = []


def create_csv(name,x):

    with open(name, 'wb') as testfile:
        csv_writer = csv.writer(testfile)

        for y in range(10):
            # print rd.uniform(-90, 90)
            csv_writer.writerow([x,y])

def read_csv(name):
    csvfile = open(name, 'rb')
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    list_groups_speed = []
    list_groups_angle = []

    for row in reader:
        #print row
        # pour chaque donne on cherche a quel groupe il appartient avec get_fuzzygroup :
        la.append(float(row[0]))
        lv.append(float(row[1]))
        list_groups_angle.append(get_fuzzygroups(float(row[0]), fuzzy_set_limit_angle))
        list_groups_speed.append(get_fuzzygroups(float(row[1]), fuzzy_set_limit_speed))
        # on fait correspondre les sous groupes avec leurs codes

    #    for i in range(len(list_groups_speed)):
    # print "listangle " + str(i) + " : " + str(la[i]), list_groups_angle[i]
    # print "listspeed " + str(i) + " : " + str(lv[i]), list_groups_speed[i]
    angle_groups.extend(list_groups_angle)
    speed_groups.extend(list_groups_speed)

def get_fuzzygroups(x,fsl):
    l_ret = []
    for element in fsl:
        low, high = element
        # print "low {}, high {}:".format(low,high)
        if x in min(fsl):
            l_ret.append(min(fsl))
            break

        elif x in max(fsl):
            l_ret.append(max(fsl))
            break

        elif low < x < high:
            l_ret.append(element)
    return l_ret


def apply_rule(angle):
    # appliquer les ET pour tout la pos et la vitesse
    fta = []
    for i in range(len(angle_groups)):
        l = angle_groups[i]
        for j in l:
            l1, l2 = j
            fta.append(fzt.FuzzyTriangle(l1, l2))
    ftv = []

    for i in range(len(speed_groups)):
        l = speed_groups[i]
        for j in l:
            l1, l2 = j
            ftv.append(fzt.FuzzyTriangle(l1, l2))
    l_codea = []
    l_codev = []
    # BOUCLE PRINCIPALE
    for listofgroups in angle_groups:
        for group in listofgroups:
            l_codea.append(getKey(dico_rule_angle, group))
    for listofgroups in speed_groups:
        for group in listofgroups:
            l_codev.append(getKey(dico_rule_speed, group))

    # print  "ruletable[{}][{}]".format(l_codea[1],l_codev[1])
    x = 0
    y = 0
    l = {NM: 0, NS: 1, ZR: 2, PS: 3, PM: 4}
    l_active = []
    for i in l_codea:
        for j in l_codev:
            lolo = 1

    # appliquer les OU pour le resultat du calcule precedemment


    return True


def getKey(dict, vals):
    for key, val in dict.items():
        if val == vals:
            return key


def main():
    # create_csv("valeur.csv",90)
    read_csv("valeur.csv")
    apply_rule(90)


if __name__ == '__main__':
    main()
    pen  = pd.Pendule(1,10)


