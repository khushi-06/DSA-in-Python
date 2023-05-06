class node:
    def __init__(self,data):
        self.data= data
        self.next=None

class linkedlist():
    def __init__(self):
        self.heaf=None

    def print (self):
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next

    




list=linkedlist()

list.head=node(1)
second=node(2)
third=node(3)

list.head.next=second
second.next=third

list.print()



