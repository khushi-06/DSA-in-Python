def bubble_Sort(a):
    for i in range (0, len(a)):
        for j in range(0,len(a)-i-1):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]



a=[1,4,5,2,9]
print("The given array is : " ,a)
bubble_Sort(a)
print("The sorted array is : " ,a)