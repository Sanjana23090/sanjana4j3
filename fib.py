def fib(n):
    if(n<2):
        return 1
    return (fib(n-1)+fib(n-2))
n=int(input("Enter no.of terms "))
for i in range(n): #evaluate upto n
    print("fibonacci (",i,")",fib(i))
    
