vdays=84
vcalls=3000
vmsg=100
vdata=2
days=int(input("Enter num of days the data is used: "))
calls=int(input("Enter num of calls used up: "))
msgs=int(input("Enter num of msgs sent: "))
data=float(input("Enter the amount of data used: "))
if(days<=vdays):
    x=vdays-days
    print("No.of days left: ", x)
    if(calls<=vcalls):
        y=vcalls-calls
        print("No.of calls left: ",y )
    else:
         print("Calls couldn't be connected")
    if(msgs<=vmsg):
        z=vmsg-msgs
        print("No.of msgs left: ",z)
    else:
        print("Msgs can't be sent")
    if(data<=vdata):
        w=vdata-data
        print("Data left: ",w)
    else:
        print("No data left")
else:
    print("Your data plan is already expired")
