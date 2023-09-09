#QUESTION: S1 AND S2 ARE GIVEN STRINGS,CREATE A FUNCTION TO FIND THE LENGTH OF THE LONGEST SUBSEQUENCE 
# WHICH IS COMMON TO BOTH STRINGS.

def LCSlength(s1,s2,lens1,lens2):
    if lens1==0 or lens2==0:
        return 0
    if s1[lens1-1]==s2[lens2-1]:
        return 1+ LCSlength(s1,s2,lens1-1,lens2-1)
        
    return max(LCSlength(s1,s2,lens1,lens2-1), LCSlength(s1,s2,lens1-1,lens2))