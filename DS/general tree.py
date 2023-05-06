class treenode():
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def print_tree(self):
        print(self.data)
        for child in self.children: 
            # print(child.data)
            child.print_tree()




def  product_tree():
    # root is object 
    root=treenode("electronic")
    # new ovject lapptop 
    laptop=treenode("laptop")
    # in the root object added laptop as a child
    root.add_child(laptop)

    laptop.add_child(treenode("lenovo"))
    laptop.add_child(treenode("Hp"))
    laptop.add_child(treenode("dell"))
    laptop.add_child(treenode("acer"))

    mobile=treenode("mobile")
    root.add_child(mobile)
    mobile.add_child(treenode("mi"))
    mobile.add_child(treenode("realme"))
    mobile.add_child(treenode("iphone"))

    tv=treenode("tv")
    root.add_child(tv)
    tv.add_child(treenode("samsung"))
    tv.add_child(treenode("lg"))
    tv.add_child(treenode("videocon"))

    return root


if __name__=='__main__':
    root=product_tree()
    root.print_tree()
    pass
        