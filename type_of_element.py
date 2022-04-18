list=['7',4,9,True,2.5]
i=0
a=[]
b=[]
c=[]
d=[]
while i<len(list):
    if type(list[i])==str:
        a.append(list[i])
    elif type(list[i])==int:
        b.append(list[i])
    elif type(list[i])==bool:
        c.append(list[i])
    elif type(list[i])==float:
        d.append(list[i])
    i=i+1
print("string=",a)
print("integer=",b)
print("tuple=",c)
print("float=",d)
