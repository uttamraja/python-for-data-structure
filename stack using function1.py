stack =[]
n = int(input("Enter the limit of list"))
def push():
    if len(stack) == n:
        print("list is full !!")
    else:
        element = int(input("Enter the element"))
        stack.append(element)
        print(stack)
def pop_element():
    if not stack:
        print("list is empty !!")
    else:
        e=stack.pop()
        print("popped element is ", e)
        print(stack)

while True:
    print("Enter 1.pop 2.push 3.quit")
    choice =int(input())
    if (choice ==1):
        push()
    elif (choice == 2):
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct option")
