# coding=utf-8
import csv

import pendule as pd
from rule import Rule
"""
    Principe de l'evaluation :
        - en binome
        - programmation d'un systeme de controle floue pour un pendule inverse
        - ENTRES : - angle de la tige par rapport verticale
                   - vitesse angulaire (calculé)
"""



def create_csv(name,x):

    with open(name, 'wb') as testfile:
        csv_writer = csv.writer(testfile)

        for y in range(10):
            # print rd.uniform(-90, 90)
            csv_writer.writerow([x,y])

def read_csv(name):
    csvfile = open(name, 'rb')
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    list_speed = []
    list_angle = []

    for row in reader:
        #print row
        # pour chaque donne on cherche a quel groupe il appartient avec get_fuzzygroup :
        list_angle.append(float(row[0]))
        list_speed.append(float(row[1]))
    return list_angle, list_speed

def main():
    # create_csv("valeur.csv",90)
    l1, l2 = read_csv("valeur.csv")
    rule = Rule()

    for i in range(len(l1)):
        rule.apply_rule(l1[i], l2[i])



if __name__ == '__main__':
    main()
    pen  = pd.Pendule(1,10)


