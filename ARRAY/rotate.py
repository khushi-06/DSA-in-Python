# LEFT ROTATION IN THE ARRAY:
arr=[1,2,3,4,5,6,7]
# rotate from index 2
shift=2
# no. of shift

for i in range(0,shift):
    temp=arr[0]
    for j in range(0,(len(arr)-1)):
        arr[j]=arr[j+1]
    arr[len(arr)-1]=temp

print(arr)




'''
here we put the first elemnt in the temp and then shift all the othere element and them append that elemnt in the last 
again 
run this till the index of the shift 
'''


# # RIGTH ROTATION IN THE ARRAY
arr=[1,2,3,4,5,6,7]
# rotate from index 2
shift=2
# no. of shift

for i in range(0,shift):
    temp=arr[len(arr)-1]
    for j in range(len(arr)-1,0,-1):
        arr[j]=arr[j-1]
    arr[0]=temp

print(arr)







# def rotate(L, d, n):
#     k = L.index(d)
#     new_lis = []
#     new_lis = L[k+1:]+L[0:k+1]
#     return new_lis
 
 
# if __name__ == '__main__':
#     arr = [1, 2, 3, 4, 5, 6, 7]
#     d = 2
#     N = len(arr)
 
#     # Function call
#     arr = rotate(arr, d, N)
#     for i in arr:
#         print(i, end=" ")