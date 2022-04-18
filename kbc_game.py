# question_list = ["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]

# options_list = [
#  #pehle question ke liye options
#  ["Four", "Nine", "Seven", "Eight"],
#  #second question ke liye options
#  ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#  #third question ke liye options
# ["Software Engineering", "Counseling", "Tourism", "Agriculture"]]

question_list=["how many continents are there","what is capital of india","ng mei kaun se cource padhaya jaata hai"]
option_list=[["four","nine","seven","eight"],["chandigarh","bopal","chennai","delhi"],["softwear engineering","counseling","tourism","agriculture"]]
answer_list=["3","4","1"]
fifty_fifty=[["nine","seven"],["delhi","chennai"],["softwear engineering","counciling"]]
solution_list=["2","1","1"]             
i=0
while i<len(question_list):
    print(i+1,question_list[i])
    j=0
    while j<=len(option_list):
        print(j+1,option_list[i][j])
        j=j+1
    answer=(input("enter the answer"))
    if answer==answer_list[i]:
        print("congrats")
    elif answer=="5050":
        print(fifty_fifty[i])
        user=input("enter the answer")
        if user==solution_list[i]:
            print("congrats")
        else:
            print("sorry wrong answer")
            break
    else:
        print("sorry wrong answer")
    i=i+1
    











   