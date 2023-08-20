email="sanjanach@gmail.com"
pwd=123456
cemail=input("Enter the email:")
cpwd=int(input("Enter pwd:"))
if(email==cemail and pwd==cpwd):
    print("Login successfully")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to mail")
elif(email==cemail and pwd!=cpwd):
    print("login failed due to pwd")
else:
    print("Login failed due to email and pwd")
