# Write a code that works for all lists. It should print the output as the following like for all the odd numbers and all the even numbers and for all the numbers in the given list, it should calculate the following :
# count
# sum
# average
# and then print it.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_sum=0
odd_sum=0
count_even=0
count_odd=0
average_even=0
average_odd=0
total_sum=0
total_count=0
total_average=0
while i<len(elements):
    if elements[i]%2==0:
        even_sum=even_sum+elements[i]
        count_even=count_even+1
        average_even=even_sum/len(elements)
    elif elements[i]%2!=0:
        odd_sum=odd_sum+elements[i]
        count_odd=count_odd+1
        average_odd=odd_sum/len(elements)
    total_sum=even_sum+odd_sum
    total_count=count_even+count_odd
    total_average=average_even+average_odd
    i=i+1
print(even_sum)
print(count_even)
print(average_even)
print(odd_sum)
print(count_odd)
print(average_odd)
print(total_sum)
print(total_count)
print(total_average)