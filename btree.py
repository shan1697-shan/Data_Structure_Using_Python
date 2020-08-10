class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None

class Btree:
    def __init__(self):
        self.root=None

    def insert(self):
        dta=int(input("Enter the data:"))
        newnode=Node(dta)
        if self.root==None:
            self.root=newnode
        else:
            self._insert(newnode,self.root)

    def _insert(self,nw,curr):
        if curr.data<nw.data:
            if curr.right==None:
                nw.parent=curr
                curr.right=nw
                print("Data is inserted at right of",curr.data)
            else:
                self._insert(nw,curr.right)

        elif curr.data>nw.data:
            if curr.left==None:
                nw.parent=curr
                curr.left=nw
                print("Data is inserted at left of",curr.data)
            else:
                self._insert(nw,curr.left)

        else:
            print("Data Alreay exists.")

    def display(self):
        print("Tree in inorder traversal:")
        self._display(self.root)

    def _display(self,curr):
        if curr!=None:
            self._display(curr.left)
            print(curr.data)
            self._display(curr.right)

    def delnode(self):
        val=int(input("Enter the value of node to delete:"))
        self._delnode(self.root,val)

    def _delnode(self,curr,val):
        if curr!=None:
            if curr.data==val:
                if curr.left==None and curr.right==None:
                    parent=curr.parent

                    if parent.data<val:
                        parent.right=None
                    else:
                        parent.left=None

                    print(curr.data, " is deleted.")
                else:
                    print("can't delete this node.")

            else:
                if curr.data>val:
                    self._delnode(curr.left,val)

                else:
                    self._delnode(curr.right,val)

if __name__ == '__main__':
    obj = Btree()
    while True:
        choice = input("1 to insert:\n2 to "
                       "delete:\n3 to diplay:\n"
                       "4 to exit:")
        if choice=='1':
            obj.insert()
        elif choice=='2':
            obj.delnode()
        elif choice=='3':
            obj.display()
        elif choice=='4':
            exit()
        else:
            print("error!! Try again")
