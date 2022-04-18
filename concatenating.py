# Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

list=['p','q']
n=5
a=[]  
i=1
while i<=n:
    j=0
    while j<len(list):
        c=list[j]+str(i)
        a.append(c)
        j+=1
    i=i+1
print(a)