class Bsort:
    data = []

    def insert(self):
        val = int(input("Enter the data:"))
        self.data.append(val)
        choice = input("1 to enter another data\n"
                       "2 to main menu\n")
        if choice=='1':
            self.insert()
        elif choice=='2':
            return
        else:
            print("Wrong choice!!")

    def sortb(self):
        total = len(self.data)
        for i in range(total):
            for j in range((total-i-1)):
                if self.data[j]>self.data[j+1]:
                    self.data[j],self.data[j+1]=self.data[j+1],self.data[j]

    def display(self):
        self.sortb()
        print("Sorted data is:")
        for i in self.data:
            print(i)

if __name__ == '__main__':
    obj = Bsort()
    while True:
        choice = input("1 to insert:\n2 to diplay:\n"
                       "3 to exit:")
        if choice=='1':
            obj.insert()
        elif choice=='2':
            obj.display()
        elif choice=='3':
            print("Bye")
            exit()
        else:
            print("error!! Try again")