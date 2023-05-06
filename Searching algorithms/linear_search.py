def linear_search(list,n):
    count=-1
    for i in range(0,len(list)):
        if list[i]==n:
                count+=1
                print("element found at ",i)
                break
        else:
            pass

    if count==-1:
        print("not found")



list=[1,2,3,4,5]
n=4
list=linear_search(list,n)
