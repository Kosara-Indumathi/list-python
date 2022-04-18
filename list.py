list=[[2,4,6],1,10]
i=0
s=0
while i<len(list):
    j=0
    while j<len(list[i]):
       s=s+list[i][j]
       s=s+1
       j=j+1
    i=i+1
print(s)


