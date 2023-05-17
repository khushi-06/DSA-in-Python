def insertion_Sort(a):
    for i in range(1,len(a)):
        postion=i
        print("Itteration No.: " ,postion)
        print("The list is:",a)
        current_element=a[i]
        while current_element<a[postion-1] and  postion>0:
            print(a)
            a[postion]=a[postion-1]
            postion=postion-1
            print(a)   
        a[postion]=current_element
    







b=[1,4,5,2,9]
print("The given array is : " ,b)
insertion_Sort(b)
print("The sorted array is : " ,b)