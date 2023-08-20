def create_stack():
    stack=[]
    return stack
#checking empty
def check_empty(stack):
    return len(stack)==0
#adding items
def maruthipush(stack,item):
    stack.append(item)
    print("pushed item: " +item)
#removing item
def maruthipop(stack):
    if(check_empty(stack)):
        return "Stack is empty"
    return stack.pop()
stack=create_stack()
maruthipush(stack,str(10)) 
maruthipush(stack,str(20))
maruthipush(stack,str(30))
maruthipush(stack,str(40))
print("popped item: " +maruthipop(stack))
print("popped item: " +maruthipop(stack))
print("popped item: " +maruthipop(stack))
print("popped item: " +maruthipop(stack))
print("popped item: " +maruthipop(stack))
print("Stack after popping element: "+str(stack))
