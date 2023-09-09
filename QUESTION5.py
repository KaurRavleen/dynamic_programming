#QUESTION: THE SHORTEST COMMON SUPER SEQUENCE (SCS) IS THE PROBLEM OF FINDING THE SHORTEST SUPER SEQUENCE 
# SUPSEQ OF GIVEN SEQUENCES S1 AND S2 THAT BOTH THESE SEQUENCES ARE SUBSEQUENCES OF SUPSEQ.

def SCSlength(x,y,m,n):
    #if we have reached the end of either subsequence, return lenght of othrt sequence
    if m==0 or n==0:
       return m+n
    #if last character matches
    if x[m-1] == y[n-1]:
        return SCSlength(x,y,m-1,n-1)+1
    #last character of x and y doesnt match 
    return min(SCSlength(x,y,m-1,n)+1, SCSlength(x,y,m,n-1)+1) 
