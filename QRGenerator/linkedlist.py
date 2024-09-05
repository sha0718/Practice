class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None 

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
         itr = itr.next

        itr.next = Node(data,None)

    def insert_values(self,data_list):
        self.head = None
        for data in  data_list:
            self.insert_at_end(data)

    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def insert_at(self,index,data):
        if index<0 or index>=self.get_lenght():
            raise Exception("invalid index")     

        if index==0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next= itr.next.next
                break
            itr = itr.next
            count += 1       


if __name__ == '__main__':
    ll = LinkedList() 
    ll.insert_values([23,43,54,67,56])
    ll.insert_at_end(73)
    ll.print()
    