list=[2,3,7,9,1,2,3]
i=0
a=[]
while i<len(list):
    j=1
    while j<len(list):
        b=list[i]+list[j]
        a.append(b)
        j=j+1
    i=i+7
print(a)