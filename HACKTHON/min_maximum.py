list=[1,2,3,5,6]
i=0
max=0
min=list[0]
while i<len(list):
    if list[i]>max:
        max=list[i]
    elif list[i]<min:
        min=list[i]
    i=i+1
a=max-min
print(a)    

