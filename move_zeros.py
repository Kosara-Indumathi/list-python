list=[0,1,0,3,12]
i=0
c=[]
p=[]
while i<len(list):
    if list[i]>0:
        c.append(list[i])
        c.sort()
    else:
        p.append(list[i])
        p.sort()
    d=c+p
    i=i+1
print(d)