#QUESTION: CREATE A FUNCTION TO FIND THE LENGTH OF THE LONGEST REPEATED SUBSEQUENCES.IT IS LONGEST SUBSEQUENCE 
#OF A STRING THAT OCCURS AT LEAST TWICE.

def LRS(x,m,n):
    if m==0 or n==0:
        return 0
    if x[m-1]==x[n-1] and m!=n:
        return LRS(x,m-1,n-1)+1
    return max(LRS(x,m-1,n),LRS(x,m,n-1))

