# a=[13,12,11,15,16]
# print(a[2],a[1],a[0])

numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max=0
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    i=i+1
print(max)