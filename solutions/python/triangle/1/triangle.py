def is_triangle(sides):
    for s in sides:
        if s <= 0:
            return False
    
    if len(sides) != 3:
        return False
    
    return (sides[0] + sides[1] >= sides[2]) and (sides[0] + sides[2] >= sides[1]) and (sides[1] + sides[2] >= sides[0])


def equilateral(sides):
    if not is_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if not is_triangle(sides):
        return False
    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]


def scalene(sides):
    if not is_triangle(sides):
        return False
    return (sides[0] != sides[1]) and (sides[0] != sides[2]) and (sides[1] != sides[2])
