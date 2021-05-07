import math


def solve(a, b, c, alpha, beta, gamma):
    y = b * math.cos(math.radians(beta)) + a * math.sin(math.radians(alpha)) - c * math.sin(math.radians(gamma))
    x = b * math.sin(math.radians(beta)) + c * math.cos(math.radians(gamma)) - a * math.cos(math.radians(alpha))
    CO = math.sqrt(x ** 2 + y ** 2)
    ang = math.degrees(math.atan(y / x))
    tOC = 180 - ang
    d = int(tOC)
    m = int((tOC - d) * 60)
    s = int((tOC - d - m / 60) * 3600)
    res = list((round(CO), d, m, s))
    return res
