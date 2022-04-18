# Write a code that works for any list, it shows the two averages as the output. One is the average of even numbers and the other is the average of odd numbers from the given list.
list= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_sum=0
odd_sum=0
while i<len(list):
    if list[i]%2==0:
        even_sum=even_sum+list[i]
        average=even_sum/len(list)
    elif list[i]%2!=0:
        odd_sum=odd_sum+list[i]
        average1=odd_sum/len(list)
    i=i+1
print(average)
print(average1)

