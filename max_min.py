i=1
a=[]
while i<=10:
    n=int(input("enter number"))
    a.append(n)
    i=i+1
    j=0
    max=0
    smal=a[0]
    while j<len(a):
        if a[j]>max:
            max=a[j]
        elif a[j]<smal:
            smal=a[j]
        j=j+1
print(max)
print(smal)














