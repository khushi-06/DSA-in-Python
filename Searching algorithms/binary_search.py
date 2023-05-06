# define upper and lower bound of the list
# see if it is the last element left then "not found"
# if not last:
# then find the mid and check of the value is equal to mid
# if not then check less than of greater than mid:
# less than mid = l=mid+1
# grater than mid =u=mid-1




def binary_Search(list,n,l,u,f):

    while l<=u and not f:
            mid=(l+u)//2
            if list[mid]==n:
                # print(mid)
                f=True
            elif n>list[mid]:
                    l=mid+1
            else:
                u=mid-1

    if f==True:
        print("found")
        print(mid)
    else:
        print("not found")




list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
n=18
l=0
u=len(list)-1
f=False

# calling the function
x=binary_Search(list,n,l,u,f)
        


