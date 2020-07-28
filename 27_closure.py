# Python Closures
def pwr(exponent):
    def bse(base):
        return pow(base, exponent)
    return bse


sq = pwr(2)
print(sq(2))
print(sq(3))
print(sq(4))
cube = pwr(3)
print(cube(2))
print(cube(3))
print(cube(4))
