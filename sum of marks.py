# Check your program for following nested lists as well (your code should run without making any change, if its not running properly then that means that you have not written the code properly ) :

marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78]]
i=0
s=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        s=s+marks[i][j]
        j=j+1
    i+=1
print(s)
