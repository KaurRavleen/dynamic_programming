#QUESTION:GIVEN A SEQUENCE FIND THE LENGTH OF THE LONGEST PALINDROME SUBSEQUENCE IN IT USING DYNAMIC PROGRAMMING.

def lps(str):
    n=len(str)
    l=[[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        l[i][i]=1
    for c1 in range(2,n+1):
        for i in range(n-c1+1):
            j=i+c1-1
            if str[i]==str[j] and c1==2:
                l[i][j]=2
            elif str[i]==str[j]:
                l[i][j]=l[i+1][j-1]+2
            else:
                l[i][]=max(l[i][j-1],l[i+1][j])
        return l[0][n-1]                