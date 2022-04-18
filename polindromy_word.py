# A palindrome is a word, sentence, verse, or even a number that reads the same backward or forward. Like NITIN. Read Nitin either from left or right, it will be same. Similarly MOM is also a palindrome.
# Write a code that checks whether a list is a palindrome or not. And print “Haan! palindrome hai” if its a pallindrome and “nahi! palindrome nahi hai” if its not a palindrome.
# For the time being you can use the list given below for writing the code.

list=[ 'n','i','t','i','n' ]
i=1
a=[]
while i<=len(list):
    b=list[-i]
    a.append(b)
    i=i+1
print(a)
if list==a:
    print("polindrome")
else:
    print(" not polindrome")

