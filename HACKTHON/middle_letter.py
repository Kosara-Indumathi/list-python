string=("abc")
i=0
while i<len("abc"):
    if len(string)%2==0:
       print(" ") 
    else:
        i=int(len(string)//2)
        print(repr(string[i:i+1]))
    i=i+1




