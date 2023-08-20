import re
str1="she sells sea shells at sea shore"
p1='sea'
rep='ocean'
ns=re.sub(p1,rep,str1,2)
print(ns)
ns=re.sub(p1,rep,str1,1)
print(ns)
