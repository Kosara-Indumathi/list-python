# When index i is there, then what will be at index length - i -1.
# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# i	places[i]	length - i	places[length - i]
# 0	"delhi"	4	"kerala"
# 1	"gujrat"	3	"punjab"
# 2	"rajasthan"	2	"rajasthan"
# 3	"punjab"	1	"gujrat"
# 4	"kerala"	0	"delhi"


places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
rev=len(places)-1
while rev>=0:
       print(places[rev])
       rev-=1

        