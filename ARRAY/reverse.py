# reversing a array (basic logic to reverse any thing)----------------------------
arr=['a','b','c','d']
def func():
    n=arr
    i=0
    j=4-1
    while i<j:
        t=arr[i]
        arr[i]=arr[j]
        arr[j]=t
        i+=1
        j-=1
    print(arr)


# calling the function
func()


# built-in fuction-----------------------------------------
# arr.reverse()
# print(arr)


