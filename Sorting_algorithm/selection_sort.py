# here the whole aaray is been traverse and then the minimum no. is found out 
# and then its swap with the first valuE INDEX AND THE INDEX IS INCREMNETED AND THE SAME PROCESS IS REPATED AGAIN 


def selection_sort(A):


    for i in range (0,len(A)):
        min=i
        for j in range (i+1,len(A)):
            if A[j]<A[min]:
                min=j
            temp=A[i]
            A[i]=A[min]
            A[min]=temp
    return A
    
        
 
        
A=[1,22,3,6,4]
print("The given array is : " ,A)
B=selection_sort(A)   
# Here B is a object that is calling the selection sort function

print("The sorted array is : " ,B)




