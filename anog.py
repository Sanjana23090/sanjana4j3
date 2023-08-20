str1="silent"
str2="listen"
if(len(str1)==len(str2)):
    if(sorted(str1)==sorted(str2)):
        print("Anogram")
    else:
        print("Not an anogram")
else:
    print("not anogram as length differs")
