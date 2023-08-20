def checksvalid(str1):
    count=0
    ans=False
    for i in str1:
        if i =="(" or i =="{" or i =="[":
            count +=1
        elif i ==")" or i =="}" or i =="]":
            count -=1
        if count<0:
            return ans
    if count==0:
        return not ans
    return ans
str1=input("Enter the input string: ")
print("Checks the input string valid or not? : ",checksvalid(str1))
