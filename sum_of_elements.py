num=[1,2,3,4]
i=0
s=0
c=[]
while i<len(num):
    s+=num[i]
    c.append(s)
    i=i+1
print(c)