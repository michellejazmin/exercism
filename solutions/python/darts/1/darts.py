def score(x, y):
    r = radius(x,y)
    if r > 10:
        return 0
    if r > 5:
        return 1
    if r > 1:
        return 5
    return 10

def radius(x, y):
    return (x**2 + y**2)**0.5