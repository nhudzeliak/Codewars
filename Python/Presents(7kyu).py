def presents(a):
    result = [None] * len(a)
    for i in range(len(a)):
        result[a[i]-1] = i + 1
    return result
