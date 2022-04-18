list="indumathi kosara"
i=0
c=[]
p=[]
while i<len(list):
    a=list.count(list[i])
    b=list[i],a
    c.append(b)
    if c[i] not in p:
        p.append(c[i])
    i=i+1
print(p)
                                                                           











