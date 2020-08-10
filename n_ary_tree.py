class Node:
    def __init__(self,data):
        self.data=data
        self.child=[]
        self.rooot=None

class N_ary:
    def __init__(self):
        self.root=None

    def insert(self):
        dta=input("Enter the data:")
        newnode=Node(dta)
        if self.root==None:
            self.root=newnode
        else:
            nodeval = input("Enter the value of node where you want to insert:")
            if self.root.data==nodeval:
                newnode.rooot=self.root
                self.root.child.append(newnode)
            else:
                self.findinsert(self.root,nodeval,newnode)

    def findinsert(self,curr,nodeval,nw):
        for i in curr.child:
            if i.data==nodeval:
                nw.rooot=i
                i.child.append(nw)
            else:
                curr=i
                self.findinsert(curr,nodeval,nw)

    def display(self):
        if self.root==None:
            print("No nodes are available in tree.")
        else:
            print("Root is",self.root.data)
            self.finddisp(self.root)

    def finddisp(self,curr):
        if len(curr.child)!=0:
            for i in curr.child:
                print(i.data)
                if len(i.child)!=0:
                    print("Child of",i.data)
                    curr=i
                    self.finddisp(curr)

        else:
            return

    def removenode(self):
        val=input("Enter the value of node to remove:")
        if self.root.data==val:
            if len(self.root.child)==0:
                self.root=None
            else:
                print("Can't delete the root node now.")
        else:
            self.finddel(self.root,val)

    def finddel(self,curr,val):
        for i in curr.child:
            if i.data == val:
                if len(i.child) == 0:
                    rott =i.rooot
                    count=0
                    for j in rott.child:
                        if j.data==val:
                            break
                        else:
                            count+=1
                    rott.child.pop(count)
                    break
                else:
                    print("Can't delete the root node now.")
            else:
                curr=i
                self.finddel(curr,val)

if __name__ == '__main__':
    obj = N_ary()
    while True:
        choice = input("1 to insert:\n2 to "
                       "delete:\n3 to diplay:\n4 to exit:")
        if choice=='1':
            obj.insert()
        elif choice=='2':
            obj.removenode()
        elif choice=='3':
            obj.display()
        elif choice=='4':
            exit()
        else:
            print("error!! Try again")
