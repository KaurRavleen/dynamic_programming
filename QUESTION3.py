#QUESTION: S1 AND S2 ARE GIVEN STRINGS, CREATE A FUNCTION TO PRINT ALL POSSIBLE LONGEST SUBSEQUENE WHICH IS 
#COMMON TO BOTH STRINGS.

def LCS(x,y,m,n,T):
    if m==0 or n==0:
        return str()
    if x[m-1]==y[n-1]:
        return LCS(x,y,m-1,n-1,T)+x[m-1]
    if T[m-1][n]>T[m][n-1]:
        return LCS(x,y,m-1,n,T) 
    else:
        return LCS(x,y,m,n-1,T)
    
def LCSlength(x,y,m,n,T):
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                T[i][j]=T[i-1][j-1]+1
            else:
                T[i][j]=max(T[i][j-1],T[i-1][j])
                        
     