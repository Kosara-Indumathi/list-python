input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# Count = 5 #because [1,2,5,8,4] are unique values.
i=0
c=0
a=[]
while i<len(input_list):
    if input_list[i] not in a:
        a.append (input_list[i])
        c=c+1
    i=i+1
print(c)






