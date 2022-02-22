list=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
c=0
while i<len(list):
    if 20<list[i] and 40>list[i]:
        c=c+1
    i=i+1
print(c)

