#creating empty list

stack = []

#adding  element in the empty list


stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.append(20)
stack.append(9)
stack.append(12)
#printing the list

print(stack)

#sorting the element in the list
stack.sort()


#printing the list after sorting

print(stack)



#poping  the element from the list


stack.pop()#It will pop the last element of the list 

print(stack)

print(len(stack)==0) #checking whether list is empty or not

print(stack[-1]) #It will print the  last element of the list


