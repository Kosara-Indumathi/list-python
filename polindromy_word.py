# A palindrome is a word, sentence, verse, or even a number that reads the same backward or forward. Like NITIN. Read Nitin either from left or right, it will be same. Similarly MOM is also a palindrome.
# Write a code that checks whether a list is a palindrome or not. And print “Haan! palindrome hai” if its a pallindrome and “nahi! palindrome nahi hai” if its not a palindrome.
# For the time being you can use the list given below for writing the code.

name=[ 'n', 'i', 't', 'i', 'n' ]
list=0
rev=len(name)-1
while rev>=0:
    print(name[rev],end="")
    rev=rev-1
if name==name:
    print(" haan! polindrome hai ")
else:
    print(" nahi! polindrome nahi hai ")