email="san@gmail.com"
pwd=123
cemail=input("Enter the email:")
cpwd=int(input("Enter pwd:"))
if(email==cemail and pwd==cpwd):
    print("Login successfully")
    otp=int(input("Enter otp: "))
    if(otp==5478):
        print("Order placed successfully")
    else:
        print("Order failed due to otp mismatch")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to mail")
elif(email==cemail and pwd!=cpwd):
    print("login failed due to pwd")
else:
    print("Login failed due to email and pwd")
