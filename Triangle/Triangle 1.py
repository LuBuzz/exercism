def equilateral(sides):
    return bool(sides[0]==sides[1]==sides[2]!=0)


def isosceles(sides):
    p1 = bool(sides[0]+sides[1]>=sides[2])
    p2 = bool(sides[1]+sides[2]>=sides[0])
    p3 = bool(sides[2]+sides[0]>=sides[1])
    if p1 and p2 and p3:
        if sides[0]==sides[1]:
            return True
        if sides[0]==sides[2]:
            return True
        if sides[1]==sides[2]:
            return True
        return False
    return False
    

def scalene(sides):
    p1 = bool(sides[0]+sides[1]>=sides[2])
    p2 = bool(sides[1]+sides[2]>=sides[0])
    p3 = bool(sides[2]+sides[0]>=sides[1])
    if p1 and p2 and p3:
        if sides[0]==sides[1]:
            return False
        if sides[0]==sides[2]:
            return False
        if sides[1]==sides[2]:
            return False
        return True
    return False
        
