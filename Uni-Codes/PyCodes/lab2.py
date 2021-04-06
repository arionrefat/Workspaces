class Node:
    def __init__(self, e, n):
        self.element = e
        self.next = n

class MyList:
    def __init__(self,a=None):
        self.head=None
        if a==None:
            self.head=None
        elif isinstance(a, list):
            tail = None
            for i in range(0, len(a)):
                n = Node(a[i], None)
                if(self.head is None):
                    self.head = n
                    tail = n
                else:
                    tail.next = n
                    tail = n
        elif isinstance(a,MyList):
            tail = None
            self.head=None
            n = a.head
            while(n != None):
                temp = Node(n.element, None)
                if( self.head is None):
                    self.head = temp
                    tail = temp
                else:
                    tail.next = temp
                    tail = temp
                n = n.next
    def nodeAt(self,index):
        n = self.head
        for i in range(0,index):
            n = n.next
        return n
    def size(self):
        count = 0
        n = self.head
        while n is not None:
            count = count + 1
            n = n.next
        return count
    def showList(self):
        n=self.head
        if n == None:
            print('Empty List')
        else:
            while n != None:
                print(n.element,end=" ")
                n = n.next
        print()
    def isEmpty(self):
        n=self.head
        count=0
        while(n is not None):
            count+=1
            n=n.next
        if(count>0):
            print("false")
        else:
            print("true")
    def clear(self):
        self.head=None
    def insert(self, newElement):
        n=self.head
        flag=True
        while(n is not None):
            if(n.element==newElement.element):
                flag=False
                break
            n=n.next
        if(flag==False):
            print("element already exists")
        else:
            n=self.head
            while(n.next is not None):
                n=n.next
            n.next=newElement
    def insert1(self , newElement1 , index):
        if(index<0 or index>self.size()):
            raise Exception("Invalid index")
        n=self.head
        flag=True
        while(n is not None):
            if(n.element==newElement1):
                flag=False
                break
            n=n.next
        if(flag==False):
            print("element already exists")
        else:
            newNode = Node(newElement1, None)
            if (index==0):
                newNode.next = self.head
                self.head = newNode
            else:
                pred = self.nodeAt(index-1)
                newNode.next = pred.next
                pred.next = newNode
    def remove(self, deletekey):
        n=self.head
        index=0
        for i in range(0,self.size()):
            if (n.element==deletekey):
                break
            else:
                n=n.next
                index+=1
        removedValue=self.nodeAt(index)
        removedNode = None
        if (index==0):
            removedNode = self.head
            self.head = self.head.next
        else:
            pred = self.nodeAt(index-1)
            removedNode = pred.next
            pred.next = removedNode.next
        return removedValue
    def even(self):
        n=self.head
        nH=None
        nT=None
        while(n is not None):
            if (n.element%2==0):
                temp=Node(n.element,None)
                if(nH==None):
                    nH=temp
                    nT=temp
                else:
                    nT.next=temp
                    nT=temp
            n=n.next
        temp=MyList()
        temp.head=nH
        return temp
    def findEle(self,num):
        n=self.head
        while(n is not None):
            if(n.element==num):
                return True
            n=n.next
        return False
    def reverse(self):
        newHead = None
        n = self.head
        while(n is not None):
            nextNode = n.next
            n.next = newHead
            newHead = n
            n = nextNode
        self.head=newHead
    def printSum(self):
        sums=0
        n=self.head
        while (n is not None):
            sums+=n.element
            n=n.next
        print(sums)
    def rotate(self,instruction,difference):
        if(instruction=="right"):
            difference=self.size()-difference
        for i in range(0,difference):
            oldHead = self.head
            self.head = self.head.next
            tail = self.head
            while(tail.next is not None):
                tail = tail.next
            tail.next = oldHead
            oldHead.next = None
    def sorting(self):
        size1=self.size()
        tail=None
        n=self.head
        while(n is not None):
            tail=n
            n=n.next
        for i in range(0,size1+1):
            n1=self.head
            while(n1 is not None):
                if(n1 is not tail):
                    if(n1.element>n1.next.element):
                        temp=n1.element
                        n1.element=n1.next.element
                        n1.next.element=temp
                n1=n1.next

class Tester:
    arr=[80,3,2,4,1,7,5,10,19,9]
    emp_lst=MyList()
    arr_lst=MyList(arr)
    lst_lst=MyList(arr_lst)
    emp_lst.showList()
    arr_lst.showList()
    lst_lst.showList()
    arr_lst.isEmpty()
    # copy=arr_lst
    # copy.clear()
    # copy.isEmpty()
    n=Node(11,None)
    arr_lst.insert(n)
    arr_lst.showList()
    arr_lst.insert1(3,2)
    arr_lst.showList()
    arr_lst.remove(3)
    arr_lst.showList()
    evens=arr_lst.even()
    evens.showList()
    print(arr_lst.findEle(31))
    print(arr_lst.findEle(2))
    evens.reverse()
    evens.showList()
    evens.sorting()
    evens.showList()
    arr_lst.printSum()
    arr_lst.showList()
    arr_lst.rotate("left",3)
    arr_lst.showList()
    arr_lst.rotate("right",2)
    arr_lst.showList()
