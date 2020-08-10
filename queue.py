class Queue:
    top = -1
    bottom = -1
    quearr = []
    # here top will show the index of the item or element at the top
    #of the queue and bottom will contain the bottom element's index
    def insrt(self,data,lngth):
        # forgot about that earlier if length is 5 then top will go from 0 to 4 and so we need to check if top == (5-1) to check if queue is full or not and since its not circular queue so once top is at 4 we can't change it.
        if self.top==(lngth-1):
            print("Queue is Full!!")
        else:
            self.quearr.append(data)
            self.top+=1
     #here if the top variable represents the equal quantity
    # as desired by the user then the queue will not take more
    #input

    def delet(self):
        if len(self.quearr)==0:
            print("Queue is empty.")
        # here we are using len function to check if there are
        #  elements present in queue or not if 0 elements are present the it will print queue is empty
        else:
            var = self.quearr.pop(0)
            self.bottom +=1
            #pop function can take a variable which will be index from where element is to be popped
            #since queue is first in first out so we need to pop first element every time
            print(var," is popped from ",self.bottom)

    def disp(self):
        if len(self.quearr)==0:
            print("queue is empty")

        else:
            print(self.quearr)
            # this will print the queue as a list
            # to print each element separately we need use some loop
            for i in self.quearr:
                print(i)

if __name__ == '__main__':
    obj = Queue()
    # obj is the object of the Queue class we need to create this to use the functions of the Queue class
    length = int(input("Enter the length of the queue:"))
    # this variable will contain the length of the queue.
    while True:
        choice = input("Enter 1 to insert:\n2 to delete:\n3 to display:\n4 to exit:")
        if choice=='1':
            dta = input("enter the data:")
            obj.insrt(dta,length)
        elif choice=='2':
            obj.delet()
        elif choice=='4':
            print("Bye!! have a nice day.")
            exit()
        elif choice=='3':
            obj.disp()
        else:
            print("wrong input please try again.")
