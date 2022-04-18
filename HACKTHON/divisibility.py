list=[85,25,65,21,84]
i=0
s=0
while i<len(list):
    if list[i]%10==0:
        print("yes")
    else:
        a=list[i]%10
        s=s*10+a
        print("last digit is",a)
    i=i+1
print(s)
if s%10==0:
    print("yes")
else:
    print("no")