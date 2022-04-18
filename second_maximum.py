numbers = [10,20,30,40,50,60,80,1000]
i=0
max=0
sec_max=0
while i<len(numbers):
    if numbers[i]>max:
        sec_max=max
        max=numbers[i]
    elif numbers[i]>sec_max and sec_max<max:
        sec_max=numbers[i]
    i=i+1
print(max)
print(sec_max)

