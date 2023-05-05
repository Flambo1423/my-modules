def c2f(x) :
    temp = (x * 9/5) + 32
    return temp

def f2c(x) :
    temp = ( x - 32) * 5/9
    return temp

def btwn(x,y,z) :
    if x >= y and x <= z :
        return('true')
    else :
        return('false')

def smldif() :
    dice = randint(1,10)
    if dice >= 5 :
        return randint(1,5)
    if dice <= 6 :
        return randint(6,10)