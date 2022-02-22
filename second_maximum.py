numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max=0
sec_max=0
while i<len(numbers):
    if numbers[i]>max:
       max=numbers[i] 
    elif numbers[i]>sec_max and sec_max<max:
        sec_max=numbers[i]
    i=i+1
print(sec_max)

