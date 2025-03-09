# 날짜가 있는지 확인해야 함 -> 여기서 년 윤년 체크 
# 날짜가 있으면 무슨 달인자 확인, 없으면 -1 

Y,M,D = map(int, input().split())

month = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leaf_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leafYear(Y):
    if Y % 4 == 0 and Y % 100 == 0 and Y % 400 == 0:
        return True
    
    if Y % 4 == 0 and Y % 100 == 0 :
        return False
    
    if Y % 4 == 0 :
        return True

    return False
        
    



def exists(Y,M,D):
    if leafYear(Y):
        if M not in month: # 존재하지 않는 달일 때 
            return False
        
        if leaf_day[M] < D: # 해당 달의 날짜보다 일이 클 때 
            return False

    
    else:
        if M not in month: # 존재하지 않는 달일 때 
            return False
        
        if day[M] < D: # 해당 달의 날짜보다 일이 클 때 
            return False
        
    return True
        






def season(Y,M,D):
    if not exists(Y,M,D):
        return "-1"
    
    if 3<=M<=5 :
        return "Spring"
    elif 6<=M<=8:
        return "Summer"
    elif 9<=M<=11:
        return "Fall"
    else:
        return "Winter"


print(season(Y,M,D))