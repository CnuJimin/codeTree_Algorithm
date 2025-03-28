x1,y1,x2,y2 = tuple(map(int, input().split()))
a1,b1,a2,b2 = tuple(map(int, input().split()))


def overlap(x1,y1,x2,y2,a1,b1,a2,b2):
    if x2 < a1:
        return False
    
    if a2 < x1:
        return False
    
    if y2 < b1:
        return False
    
    if b2 < y1:
        return False
    
    return True 




if overlap(x1,y1,x2,y2,a1,b1,a2,b2):
    print("overlapping")
else:
    print("nonoverlapping")