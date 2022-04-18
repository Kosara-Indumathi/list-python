list=[[1,2,3,],[4,5,6],[7,8,9]]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        a=list[i][j]
        print(a,end=",")
        j=j+1
    i=i+1