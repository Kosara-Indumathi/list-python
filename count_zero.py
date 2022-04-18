list=[1,2,0,3,4,0,7,6,0]
i=0
c=[]
p=[]
count=0
while i<len(list):
    if list[i]>0:
        c.append(list[i])
        c.sort()
    else:
        p.append(list[i])
        p.sort()
        count=count+1
    d=c+p
    i=i+1
print(d,count)