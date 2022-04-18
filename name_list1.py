list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
i=0
a=[]
while i<len(list1):
    j=0
    while j<len(list2):
        b=list1[i]+list2[j]
        a.append(b)
        j=j+1
        i=i+1
    print(a)



