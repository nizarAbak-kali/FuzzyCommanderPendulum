import csv

import pendule as pd

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

dico_rule = {NM: (-90, -30), NS: (-60.0, 0.0), ZR: (-30.0, 30.0), PS: (0.0, 60.0), PM: (30.0, 90.0)}

def create_csv(name,x):

    with open(name, 'wb') as testfile:
        csv_writer = csv.writer(testfile)
        for y in range(10):
            csv_writer.writerow([x,y])

def read_csv(name):
    csvfile = open(name, 'rb')
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

    for row in spamreader:
        print row
        # pour chaque donne on cherche a quel groupe il appartient avec get_fuzzygroup :
        #  list_groups = get_fuzzygroups()
        # on fait correspondre les sous groupes avec leurs codes
        # return


def get_fuzzygroups(x,fsl):
    l_ret = []
    for element in fsl:
        low, high = element
        if (x >= low and x <= high):
            l_ret.append(element)
    return l_ret


def apply_rule(angle):
    # appliquer les ET pour tout la pos et la vitesse

    # appliquer les OU pour le resultat du calcule precedemment


    return True

def main():
    create_csv("valeur.csv",90)
    fuzzy_set_limit = [(-90.0, -30.0), (-60.0, 0.0), (-30.0, 30.0), (0.0, 60.0), (30.0, 90.0)]



if __name__ == '__main__':
    main()
    pen  = pd.Pendule(1,10)


