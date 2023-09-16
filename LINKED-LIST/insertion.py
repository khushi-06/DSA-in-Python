# # insertion can be done in three ways:
# # 1.head
# # 2.middle(insert)
# # 3.tails(append)



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
    
    def insert_head(self,value):
        # by calling the node class we create a new node and pass the data
        new_node=node(value)
        # now we link the new node to the head. hence we insert the item using the head
        new_node.next=self.head
        self.head=new_node
        self.n=self.n+1

    
    def __len__(self):
        return self.n

    def insert_after(self,after,value):
        new_node=node(data)
        curr=self.head
        while curr!=None:
            if curr==after:
                break
            print()


l=linkedlist()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.insert_head(3)

# print(len(l))
























