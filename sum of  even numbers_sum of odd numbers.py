# Write a code that works for any list, it should give two sums as outputs, one is the sum of odd numbers present in the list and the other is the sum of even numbers present in the list.
list = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_sum=0
odd_sum=0
while i<len(list):
    if list[i]%2==0:
       even_sum=even_sum+list[i]
    elif list[i]%2!=0:
        odd_sum=odd_sum+list[i]
    i=i+1
print(even_sum)
print(odd_sum)
    

