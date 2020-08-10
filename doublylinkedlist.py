class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Dlinked:
    curr = Node(None)

    def __init__(self):
        self.head = None

    def insert(self):
        val=input("Enter the data:")
        newnode = Node(val)
        if self.head == None:
            self.head = newnode
        else:
            newnode.prev = self.curr
            self.curr.next = newnode

        self.curr = newnode

    def insert_at(self):
        val = input("Enter the data:")
        newnode = Node(val)
        pos = int(input("Enter the position to insert data:"))
        ptr = None
        for i in range(1,pos):
            if self.curr.next==None:
                self.curr.next = newnode
                newnode.prev = self.curr
                return
            else:
                ptr = self.curr
                self.curr = self.curr.next

        ptr.next = newnode
        newnode.prev = ptr
        newnode.next = self.curr
        self.curr.prev = newnode

    def displayall(self):
        self.curr = self.head
        while True:
            print(self.curr.data)
            if self.curr.next == None:
                return
            else:
                self.curr= self.curr.next


    def dispone(self):
        self.curr = self.head
        print(self.curr.data)
        while True:
            choice = input("1 for previous:\n2 for next:\n3 to return to"
                           "main menu:")
            if choice=='1':
                if self.curr.prev==None:
                    print("No previous node.")
                else:
                    self.curr = self.curr.prev
                    print(self.curr.data)
            elif choice=='2':
                if self.curr.next==None:
                    print("No previous node.")
                else:
                    self.curr = self.curr.next
                    print(self.curr.data)
            elif choice=='3':
                return
            else:
                print("wrong choice")

    def remfrom(self):
        self.curr = self.head
        pos = int(input("Enter the position to insert data:"))
        ptr = None
        for i in range(1, pos):
            if self.curr.next == None:
                print("Node Does Not Exists.")
                return
            else:
                ptr = self.curr
                nxt = self.curr.next
                self.curr = self.curr.next



        ptr.next = self.curr.next
        nxt.prev = ptr
        print("node removed is:",self.curr.data)


if __name__ == '__main__':
    obj = Dlinked()
    while True:
        choice = input("1 to insert:\n2 to insert at position:\n"
                       "3 to delete:\n4 to diplay:\n5 to display one"
                       "by one:\n6 to exit:")
        if choice == '1':
            obj.insert()
        elif choice == '2':
            obj.insert_at()
        elif choice == '3':
            obj.remfrom()
        elif choice == '4':
            obj.displayall()
        elif choice == '5':
            obj.dispone()
        elif choice == '6':
            exit()
        else:
            print("error!! Try again")
