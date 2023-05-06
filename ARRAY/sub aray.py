# here we get output as interger

arr=[1,2,3,4]
n=len(arr)
for i in range(n):
    for j in range(i,n):
        for k in range(i,j):
            print(arr[k])
        print()

# output as array itself:

