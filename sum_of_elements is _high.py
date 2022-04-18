# Write a Python program to find the list in a list of lists 
# whose sum of elements is the highest. Go to the editor
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]

list=[1,2,3],[4,5,6],[10,11,12],[7,8,9]
i=0
while i<len(list):
    j=0
    a=[]
    while j<len(list[i]):
        a.append(sum(list[j]))
        j+=1
    i+=1
k=0
while k<len(list):
    if sum(list[k])==max(a):
        print(list[k])
    k+=1


