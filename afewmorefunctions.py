def isEven(num):
    return (num % 2 == 0)

def isOdd(num):
    if num % 2 != 0:
        return True
    else:
        return False

def square(num):
    return num*num

def length(string):
    count = 0 
    for i in string:
        count += 1
    
    return count

def lastletter(string):
    return string[-1]
    
def bigger(numA, numB):
    if numA > numB:
        return numA
    else:
        return numB
def biggest(numA,numB,numC): 
    return bigger(bigger(numA,numB), numC)
     
