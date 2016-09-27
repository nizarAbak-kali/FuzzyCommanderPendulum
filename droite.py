class Droite():
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def getcoeff(self):
        return self.a

    def getB(self):
        return self.b

    def getY(self, x):
        return self.a * x + self.b

    def toString(self):
        text = str(self.a) + ".x + " + str(self.b)
        return text
