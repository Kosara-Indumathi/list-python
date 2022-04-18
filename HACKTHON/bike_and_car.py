n=int(input("enter the time taken by the bike:"))
n1=int(input("enter the time taken by the car:"))
i=0
while n>0:
    if n>n1:
        print("CAR")
    elif n<n1:
        print("BIKE")
    else:
        print("SAME")
    break
i=i+1