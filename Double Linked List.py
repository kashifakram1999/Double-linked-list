class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def get_last_node(self):
        if self.head==None:
            return None
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
    
    
    def print_forward(self):
        if self.head == None:
            print ("list is empty")
            return
        
        itr = self.head
        llitr =""
        while itr:
            llitr += str(itr.data) + "--->"
            itr = itr.next
        print(llitr)
    
    def print_backward(self):
        if self.head == None:
            print("list is empty")
            return
        
        last_node = self.get_last_node()
        itr = last_node
        llitr =""
        while itr:
            llitr += str(itr.data) + "-->"
            itr =itr.prev
        print(llitr)
    
    def get_length(self):
        
        count = 0
        itr= self.head
        while itr:
            count +=1
            itr = itr.next
            
        return count
    
    def prepend(self,data):
        if self.head == None:
            node = Node(data, self.head,None)
            self.head = node
        else:
            node = Node(data,self.head,None)        
            self.head.prev = node
            self.head = node
    
    def append(self,data):
        if self.head == None:
            self.head = Node(data, None,None)
            return
        
        # itr = self.head
        # while itr.next:
        #     itr=itr.next
        itr = self.get_last_node()
        itr.next=Node(data, None, itr)
        
    def insert_at(self,index,data):
        if index<0 or index> self.get_length():
            print("invalid index")
            return
        if index == 0:
            self.prepend(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next =node
                return
            itr = itr.next
            count +=1
            
    def remove_At(self,index):
        if index<0 or index> self.get_length():
            print("invalid index")
            return
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        itr = self.head
        count = 0
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr =itr.next
            count +=1
    
    def insert_values(self,data_list):
        for x in data_list:
            self.append(x)
        return 
                
        
        
dll = DoubleLinkedList()
dll.append(69)
dll.prepend(123)
dll.prepend(3)
dll.prepend(12)
dll.insert_at(3,34)
dll.print_forward()
dll.insert_values(["a","b"])
dll.print_forward()
dll.remove_At(3)
dll.print_forward()
dll.get_last_node()
print(dll.get_length())
            
        
    