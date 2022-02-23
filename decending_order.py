list=[5,2,23,6,57,32,10,25]
i=0
length=0
while i<len(list):
   if list[i]>=length:
      list.sort()
      list.reverse()
      print(list[i])
   i=i+1