numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
list_length=len(numbers)
i=0
total_numbers=0
while i<list_length:
    total_numbers=numbers[i]+total_numbers
    i=i+1
print(total_numbers)

