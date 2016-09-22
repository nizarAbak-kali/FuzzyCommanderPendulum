import pendule as pd
import csv

PM = 2
PS = 1
ZR = 0
NS = -1
NM = -2

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

def get_fuzzygroups(x,fsl):
    l_ret = []
    for element in fsl:
        low, high = element
        if (x >= low and x <= high):
            l_ret.append(element)
    return l_ret

def apply_rule(angle,fuzzy_set,set_of_rules):
#appliquer les ET pour tout la pos et la vitesse

# appliquer les OU pour le resultat du calcule precedemment
    return True

def main():
    create_csv("valeur.csv",90)
    fuzzy_set_limit = [(-90,-30), (-60,0), (-30,30), (0,60), (30,90)]



if __name__ == '__main__':
    main()
    pen  = pd.Pendule(1,10)


