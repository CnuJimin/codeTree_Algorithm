word = input()
part = input()




def is_substr(start_idx):
    n, m = len(word), len(part)

    if start_idx + m - 1 >= n :
        return False
    
    for i in range(m):
        if word[i + start_idx] != part[i]:
            return False

    return True    
    


def get_index():
    n = len(word)
    for i in range(n):
        if is_substr(i):
            return i 
            
    return -1 


print(get_index())