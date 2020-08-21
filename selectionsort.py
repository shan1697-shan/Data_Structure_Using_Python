class Ssort:
    data=[]

    def insert(self):
        val=int(input("Enter the data:"))
        self.data.append(val)
        choice=input("1 to insert another data:\n"
                     "2 to goto main menu:")
        if choice=='1':
            self.insert()
        else:
            return

    def selectionsort(self):
        length=len(self.data)
        for i in range(length):
            min_index=i

            for j in range(i+1,length):
                if self.data[min_index]>self.data[j]:
                    min_index=j

            self.data[i],self.data[min_index]=\
                self.data[min_index],self.data[i]

    def display(self):
        self.selectionsort()
        for i in self.data:
            print(i)

if __name__ == '__main__':
    obj = Ssort()
    while True:
        choice = input("1 to insert:\n2 to diplay:\n"
                       "3 to exit:")
        if choice == '1':
            obj.insert()
        elif choice == '2':
            obj.display()
        elif choice == '3':
            print("Bye")
            exit()
        else:
            print("error!! Try again")