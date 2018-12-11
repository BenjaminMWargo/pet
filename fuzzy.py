#=========Fuzzy Logic========
def mFuzzyAnd(a,b):
    return min(a,b)
def mFuzzyOr(a,b):
    return max(a,b)
def mFuzzyNot(a):
    return 1-a
def mFuzzyCheck(x):
    return (True if x>.5 else False)
#=======Slope Functuions===========
def downSlope(x,left,right):
    slope = ((-1)/(right-left))
    b = -((slope*right))
    return (slope*x) + b
def upSlope(x,left,right):
    slope = ((1)/(right-left))
    b = -((slope*left))
    return (slope*x) + b
#========Fuzzy HP=========
def mIsCritical(x):
    #Downward Line
    leftBound = 20
    rightBound = 45
    y = x.stats.hp
    if (y < leftBound):
        return 1
    elif (y>rightBound):
        return 0
    else:
        return downSlope(y,leftBound,rightBound)                 #(((-1/25)*y)+(9/5))
def mIsHurt(x):
    #peaking line
    leftBound = 35
    rightBound = 65
    peak = 50
    y = x.stats.hp
    if ((y < leftBound) or (y>rightBound)):
        return 0
    else:
        if (y<=peak):
            #upslope
            return upSlope(y,leftBound,peak)
        else:
            #downslope
            return downSlope(y,peak,rightBound)