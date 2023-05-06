
# UNSORTED AARAY
def searching_in_array(arr,a,n):
    for i in range(a):
        if arr[i]==n:
            return i 
        else:
            pass
        
        
arr=[1,2,3,4,5]
n=9
a=len(arr)

index= searching_in_array(arr,a,n)       
if index !=-1:
    print("element found at", index+1 )
else:
    print("Element not found")


# SORTED AARAY