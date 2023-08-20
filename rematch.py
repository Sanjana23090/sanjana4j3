import re
str1="she sells sea shells at sea shore"
p1="shells"
if re.match(p1,str1):
    print("Match found")
else:
    print(p1, "not found in string")
p2="she"
if re.match(p2,str1):
    print("Match found")
else:
    print(p2, "not found in string")

