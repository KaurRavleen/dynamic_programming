#QUESTION: EGG DROPPING PUZZLE.
INT_MAX= 32767
#for min number of Trials needed in worst case n=eggs, k=floors

def eggDrop(n,k):
    #A2D table where entry eggFloor[i][j] will represent min number of trails needed for i eggs and j floors
    eggFloor= [[0 for x in range(k+1)] for x in range(n+1)]
    #1 trail for 1 floor and 0 trail for 0 floor
    for i in range(1,n+1):
        eggFloor[i][1]=1
        eggFloor[i][0]=0
    for j in range(1,k+1):
        eggFloor[i][j]=j
    #fill rest of the entries using optimal substructure property
    for i in range(2,n+1):
        for j in range(2,k+1):
            eggFloor[i][j]=INT_MAX
            for x in range(1,j+1):
                res=1+ max(eggFloor[i-1][x-1], eggFloor[i][j-x])
                if res< eggFloor[i][j]:
                    eggFloor[i][j]=res
    return eggFloor[n][k]                        