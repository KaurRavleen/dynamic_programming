#QUESTION: YOU ARE GIVEN N PAIRS OF NUMBER. IN EVERY PAIR.THE FIRST NUMBER IS ALWAYS SMALLER THAN SECOND. A PAIR (C,D) 
# CAN FOLLOW (A,B) IF B<C . FIN THE LONGEST CHAIN THAT CAN BE FORMED FROM THE GIVEN SET OF PAIRS.

def __init__(self,a,b):
    self.a=a
    self.b=b

def maxChainLength(arr,n):
    max=0
    mc1=[1 for i in range(n)]
    for i in range(1,n):
        for j in range(0,i):
            if (arr[i].a> arr[j].b and mc1[i]<mc1[j]+1):
                mc1[i]=mc1[j]+1    
    for i in range(n):
        if(max<mc1[i]):
            max=mc1[i]
    return max                    