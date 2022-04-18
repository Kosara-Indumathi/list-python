# These are the marks of any student for the last three years. You have to calculate total marks for all the three years.

marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
i=0
s=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        s=s+marks[i][j]
        j=j+1
    i=i+1
print(s)