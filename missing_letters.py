a=[1,2,4,5,8,9]
i=1
while i<=len(a):
    j=0
    while j<i:
        if i not in a:
           a.append (i)
           a.sort()
        j=j+1 
    i=i+1
print(a)