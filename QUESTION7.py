#QUESTION: GIVEN A SET OF NON-NEGATIVE INTEGERS AND A VALUE SUM, DETERMINE IF THERE IS A SUBSTE OF GIVEN SET WITH SUM
# EQUAL TO GIVEN SUM.

def isSum(set,n,sum):
    #the value of subset[i][j] will be true if there is a subset of the set [0..j-1] with sum of 1
    subset=[[False for i in range(sum+1) for i in range(n+1)]]
    #if sum is 0, answer is True
    for i in range(n+1):
        subset[i][0]=True
    for j in range(1,sum+1):
        subset[0][j]=False
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if j<set[i-1]:
                subset[i][j]=subset[i-1][j]
            if j>=set[i-1]:
                subset[i][j]=(subset[i-1][j] or subset[i-1][j-set[i-1]])
    return subset[n][sum]                       