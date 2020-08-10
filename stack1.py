# We have created a python file
# What stack does it---- First in Last out

class Stack:
    top=-1
    # here we define a variable with initial value -1 this will point the top value of the stack
    # Since now stack is empty so the top is at -1
    arr=[]
    # Now we take a list where we will store the stack values
    # here we are defining a function to take input into the stack
    def inst(self,data,n):
        # data will be the value to be inserted in the Stack and n will be the length ofthe stack
        if self.top<n:
            self.arr.append(data)
            self.top+=1
            print("Data has been inserted to the stack.")
        else:
            print("Stack is Full.")

    def disp(self):
        # this function will display the stack
        if len(self.arr)==0:
            print("Stack is empty")

        else:
            print("Stcak is:")
            for i in self.arr[::-1]:
                # since stack follows first in last out so here we will show last value first
                print(i)

    def popitem(self):
        if len(self.arr)==0:
            print("Stack is Empty.")
        else:
            val=self.arr.pop()
            print(val," has been poped.")

if __name__ == '__main__':
    obj = Stack()
    l = int(input("Enter the length of the Stack:"))
    while True:
        choice = int(input("Enter 1 to push a data into the stack\n2 to pop a data from the stack\n3 to Display\n"
                           "4 to exit."))
        if choice==1:
            dta = input("Enter a Data to push into the Stack.")
            obj.inst(dta,l)
        elif choice==2:
            obj.popitem()
        elif choice==3:
            obj.disp()
        elif choice==4:
            break
        else:
            print("Wrong choice!! Try Again")


