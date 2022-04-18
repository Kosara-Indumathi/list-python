list=[4,3,"indu","naga",2.3,4.5]
i=0
a=[]
b=[]
c=[]
while i<len(list):
    if type(list[i])==int:
        d=list[i]
        a.append(d)
    if type(list[i])==str:
        e=list[i]
        b.append(e)
    if type(list[i])==float:
        f=list[i]
        c.append(f)
    i=i+1
print(a)
print(b)
print(c)
