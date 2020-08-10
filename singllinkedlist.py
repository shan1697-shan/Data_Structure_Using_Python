class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

class Slinkedlist:
    curr = Node(None)

    def __init__(self):
        self.head = None

    def insert(self):
        val = input("Enter the data:")
        newnode = Node(val)
        if self.head == None:
            self.head = newnode
        else:
            self.curr.next = newnode
        self.curr=newnode

    def insert_at(self):
        pos = int(input("Enter the Position for new data:"))
        val = input("Enter the data:")
        newnode = Node(val)
        self.curr = self.head
        for i in range(1,pos):
            if self.curr.next == None:
                self.curr.next = newnode
                return
            else:
                ptr = self.curr
                self.curr = self.curr.next

        ptr.next = newnode
        newnode.next = self.curr

    def remove_from(self):
        pos = int(input("Enter the Position for new data:"))
        self.curr = self.head
        ptr = None
        for i in range(1, pos):
            if self.curr.next == None:
                print("The position entered does not have any data.")
                return
            else:
                ptr = self.curr
                self.curr = self.curr.next

        ptr.next = self.curr.next
        print("Node Removed is:",self.curr.data)

    def display(self):
        self.curr=self.head
        while True:
            print(self.curr.data)
            if self.curr.next == None:
                return
            else:
                self.curr = self.curr.next

if __name__ == '__main__':
    obj = Slinkedlist()
    while True:
        choice = input("1 to insert:\n2 to insert at position:\n"
                       "3 to delete:\n4 to diplay:\n5 to exit:")
        if choice=='1':
            obj.insert()
        elif choice=='2':
            obj.insert_at()
        elif choice=='3':
            obj.remove_from()
        elif choice=='4':
            obj.display()
        elif choice=='5':
            exit()
        else:
            print("error!! Try again")
