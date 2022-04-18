list=[1,2,3,4,5,6]
i=0
a=[]
while i<len(list):
    b=str(list[i])+str(list[i+1])
    a.append(b)
    i=i+2
print(a)