list=[9,9,2,4,4,8,7,7,2,8,9,6,3,9]
i=0
a=[]
b=[]
while i<len(list):
    c=list.count(list[i])
    d=list[i],c
    a.append(d)
    if a[i] not in b:
        b.append(a[i])
    i=i+1
print(b)
