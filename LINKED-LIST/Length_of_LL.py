
class node:
    def __init__(self,data):
        self.data=data
        self.next= None

class linkedlist:
    def __init__(self):
         # creating a empty linkedlist
        self.head=  None  
        # head=none     this shows that the linkedlist is empty
        self.n=0


    def __len__(self):
        return self.n

L=linkedlist()
lenght=len(L)
print(lenght)