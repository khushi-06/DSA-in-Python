# UNSORTED AARAY
'''
the major logic to insert the value at a give specific postion 
is to shift all the element after the give postion by one 
and then insert the element'''

a=[1,2,3,4,5]
n=len(a)
e=100
print(a)
# element to be added
p=3
# postion at which element is to be added


# create a blank space in last to add the element
a.append(None)

for i in (p-1,n+1,1):
# hear n-1= index starts form zero hence size is 5 but index is 4
# heare p-2 : as index hence p=3 but index is 2 also range is n+1 to blance it we eed to -1 hence 
# p-1-1=p-2
# we want it to run in reverse hence -1 is used
    a[i]=a[ 1+i]
    a[p-1]=e

    print(a)


# SORTED AARAY