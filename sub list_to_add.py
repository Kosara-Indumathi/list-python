# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub list to add
# sub_list = ["h", "i", "j"]
# Expected Output:
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list= ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list=["h","i","j"]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        list.append(sub_list)
        i=i+1
    print(list)