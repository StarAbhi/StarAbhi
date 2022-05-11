def createStack(stack,str):
    stack.append(str)
    return stack

def isEmpty( stack ):
    return len(stack) == 0
  
def display(stack):
    for i in range(len(stack)-1, -1, -1):   
        print(stack[i], end = ' ')
    print()
  
def sort_Stack( stack ):
    stack=sorted(stack)
    return stack


if __name__ == '__main__':
    str=''
    stack=[]
    print("Enter elements in stack")
    while True:
        str=input()
        if(str !='End'):
            stack=createStack(stack,str)
        else:
            if isEmpty(stack):
                str=input("Empty Stack, Enter a valid string !")
            else:
                break
    
    print("Sorted: ")
    sortedst = sort_Stack( stack )
    display(sortedst)
    