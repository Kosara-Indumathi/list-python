# Write a Python program to create a list reflecting the modified run-length encoding from 
# a given list of integers or a given list of characters. 
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# List reflecting the modified run-length encoding from the said list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Original String:
# aabcddddadnss
# List reflecting the modified run-length encoding from the said string:
# [[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]


number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
a=[]
while i<len(n)-3:
    b=[]
    j=0
    while j<len(n):
        if n[i]+n[j]==number:
            b.append(n[i])
            b.append(n[j])
            a.append(b)
        j=j+1
    i=i+1
print(a)






    
