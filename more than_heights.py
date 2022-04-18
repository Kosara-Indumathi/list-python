heights=[4,2,7,10,5,9,7,20,6]
i=0
a=[]
while i<len(heights):
    j=0
    c=0
    while j<len(heights):
        if heights[i]<heights[j]:
            c=c+1
        j=j+1
    i=i+1
    a.append(c)
print(a)