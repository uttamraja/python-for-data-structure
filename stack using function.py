#creating empty list 

stack =[]

#creating function to push 
def push():
    element = input("Enter the element")
    stack.append(element)
    print(stack)

#creating  function to pop
def pop_element():
    if not stack:
        print("List is empty")
    else:
        e =stack.pop()
        print("popped element is:", e)
        print(stack)
while True:
    print("Enter 1.push 2.pop 3.quit")
    choice =int(input())
    if choice == 1:
        push()
    elif choice ==2:
        pop_element()
    elif choice ==3:
        break
    else:
        print("Enter the correct option")
