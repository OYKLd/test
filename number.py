def numberOne (a):
    if a <= 1 :
        return False
    for b in range(2, a):
        if a % b == 0:
            return False    
    return True        

#print(numberOne(5))
#print(numberOne(10))

def evenOdd (x):
    if x % 2 == 0:
        return True
    else:
        return False

#print(evenOdd(5))    
#print(evenOdd(4))    

