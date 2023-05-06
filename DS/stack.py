# stack can be made using list and uses the feature of list
stack=[]

# we push/append values in the stack
stack.append(2)
stack.append(4)
stack.append(6)

# this printd the content of the stack
print(stack)

# to remove the value from the stack we use pop 
# here if the index is mentioned then the specific value is poped

# stack.pop(1)

# If we use basic pop() element then it uses LIFO rules: "last in first out" 
stack.pop()

print(stack)
