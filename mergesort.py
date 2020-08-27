class Msort:
    data=[]

    def inseert(self):
        val=int(input("Enter the data:"))
        self.data.append(val)
        ch=input("1 to insert another data:\n2 to goto main menu:")
        if ch=='1':
            self.inseert()

        elif ch=='2':
            return
        else:
            print("Wrong choice!! Try again.")

    def mergesort(self,arr):
        if len(arr)>1:
            mid = len(arr)//2
            left=arr[:mid]
            right=arr[mid:]

            self.mergesort(left)
            self.mergesort(right)

            i=j=k=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    arr[k]=left[i]
                    i+=1

                else:
                    arr[k]=right[j]
                    j+=1

                k+=1

            while i<len(left):
                arr[k]=left[i]
                i+=1
                k+=1

            while j<len(right):
                arr[k]=right[j]
                j+=1
                k+=1

    def display(self):
        self.mergesort(self.data)
        print("Sorted data is:")
        for i in self.data:
            print(i)

if __name__ == '__main__':
    obj=Msort()
    while True:
        choice = input("1 to insert:\n2 to diplay:\n"
                       "3 to exit:")
        if choice == '1':
            obj.inseert()
        elif choice == '2':
            obj.display()
        elif choice == '3':
            print("Bye")
            exit()
        else:
            print("error!! Try again")