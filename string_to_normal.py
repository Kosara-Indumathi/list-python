list=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        print(list[i][j],end="")
        j=j+1
    i=i+1

    