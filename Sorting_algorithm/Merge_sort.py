# def merge_sort(array):
#     def divide_list(array):
#         if len(array)>1:
#             mid=len(array)//2
#             # here we will now divide the list into two parts form the middle 
#             # array[:mid] his function will split the list from 0 to the mid value (middle not included)
            
#             left_array=array[:mid]
#             print(left_array)

#             right_array=array[mid:]
#             print(right_array)

#             # recursive function
        
#             merge_sort(left_array)
#             merge_sort(right_array)

    # # def mergr_list(array):
    #     # TO merege the whole list
    #     i=0
    #     j=0
    #     k=0
    #     while i <len(left_array) and j<len(right_array):
    #         if left_array[i] < right_array[j]:
    #             array[k]=left_array
    #             i+=1
    #             k+=1
    #         else:
    #             array[k]=right_array
    #             j+=1
    #             k+=1
    #     while i <len(left_array) and j<len(right_array):
            
    #             array[k]=left_array
    #             i+=1
    #             k+=1
    #     while i <len(left_array) and j<len(right_array):
            
    #             array[k]=right_array
    #             j+=1
    #             k+=1


def merge_list(a,b):
    sorted_list=[]
    len_a=len(a)
    len_b=len(b)
    i=j=0

    while i< len_a and j< len_b:
        if a[i]<b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1
    print(sorted_list)
    
a=[2,4,6,8]
b=[1,3,5,7]
merge_list(a, b)













# to take input form the user using the list comprehension method
# num=int(input("enter the length of array"))
# list=[int(input()) for x in range(num)]
# merge_sort(list)
# print(list)


# a=[1,4,5,2,9]
# print("The given array is : " ,a)
# merge_sort(a)
# print("The sorted array is : " ,a)