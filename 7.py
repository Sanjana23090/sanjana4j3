def checkBalance(expr):
    stack=[]
    for char in expr:
        if char in ["(","{","["]:
            stack.append(char)
        else:
            #here we check if the current character is
            #bracket,then it must be closing
            #so stack cannot be empty at this point
            print(not stack)
            if not stack:
                return False
            curr_char=stack.pop()
            if curr_char=='(':
                if char!=")":
                    return False
            if curr_char=='{':
                if char!="}":
                    return False
            if curr_char=='[':
                if char!="]":
                    return False

                if stack:
                    return false
                return true
            expr="{[9()]}"
            if checkBalance(expr):
                print("the given string is balanced")
            else:
                print("the given string is not balanced")
                    
                
