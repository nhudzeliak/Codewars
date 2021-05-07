def mygcd(x, y):
    if x == 0:
        return y
    return mygcd(y % x, x)