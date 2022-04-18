list=[1, 1, 2, 3, 4, 4, 5, 1]
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


