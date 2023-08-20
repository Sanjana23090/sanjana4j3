from collections import Counter
def check(str1,str2):
    if(Counter(str1)==Counter(str2)):
        print("True")
    else:
        print("Not")
str1='silent'
str2='listen'
check(str1,str2)
