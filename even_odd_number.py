list=[1,2,32,4,5,6,7,8,9,10]
i=0
while i<len(list):
    if list[i]%2==0:
        print(list[i],"even numbers")
    else:
        print(list[i],"odd numbers")
    i=i+1