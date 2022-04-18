char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
c=0
s=0
h=0
a=0
b=0
d=0
while i<len(char_list):
    if char_list[i]=="a":
        c=c+1
    if char_list[i]=="n":
        s=s+1
    if char_list[i]=="g":
        h=h+1
    if char_list[i]=="u":
        a=a+1
    if char_list[i]=="x":
        b=b+1
    if char_list[i]=="t":
        d=d+1
    i=i+1
print(["a",c])
print(["n",s])
print(["g",h])
print(["u",a])
print(["x",b])
print(["t",d])