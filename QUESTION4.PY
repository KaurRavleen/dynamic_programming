#QUESTION: GIVEN TWO SIMILAR STRINGS, IMPLEMENT YOUR OWN DIFF UTILITY TO LIST OUT ALL DIFFERENCES BETWEEN THEM.

def diff(s1,s2,m,n,lookup):
    #if last characters of s1 AND S2 MATCHES
    if m>0 and n>0 and s1[m-1]==s2[n-1]:
        diff(s1,s2,m-1,n-1,lookup)
        print("",s1[m-1],end="")

        #current characters of s2 is not present in s1
    elif n>0 and (m==0 or lookup[m][n-1]>=lookup[m-1][n]) :
        diff(s1,s2,m,n-1,lookup)
        print("+" + s2[n-1],end="")

        #current character of s1 is not present in s2
    elif m>0 and(n==0 or lookup[m][n-1]<lookup[m-1][n]):
        diff(s1,s2,m-1,n,lookup)
        print("-"+ s1[m-1],end="")

#Function to fill up lookup table in bottom up manner

def LCSlength(s1,s2,m,n,lookup):
    #first column and row will be 0
    for i in range(m+1):
        lookup[i][0]=0
    for j in range(n+1):
        lookup[0][j]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            #if current character of s1 and s2 matches
            if s1[i-1]==s2[j-1]:
                lookup[i][j]=lookup[i-1][j+1]+1
            #else if they are different
            else:
                lookup[i][j]=max(lookup[i-1][j],lookup[i][j-1])
                                   