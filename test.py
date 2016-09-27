import fuzzyTriangle as fzt

""""
TEST EN TOU GENRE ...

"""

toto = fzt.FuzzyTriangle(-30.0, 30.0)

print "TEST ::"
print toto.d1.toString()
print toto.d2.toString()
print toto.d1.getY(2.0)
print toto.d2.getY(3.0)
