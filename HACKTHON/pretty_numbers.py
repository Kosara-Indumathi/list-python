num=int(input("enter the first number:"))
num1=int(input("enter the second number:"))
c=0
while num<num1:
    if num%10==2 or num%10==3 or num%10==9:
        c=c+1
    num=num+1
print(c)
