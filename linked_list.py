class Node:
    def __init__(self, data = None, next = None):
        self.data = data    
        self.next = next
        
    #itr we are using is just ap loop variable to iterate through the linked list    
    #   LinkedList:
    #/ What we learned here is that a linked list is made up of nodes where each node contains data and a pointer to the
    # next node in the list.
    # The LinkedList class manages the nodes and provides methods to manipulate the list, such as inserting, deleting, 
    # and traversing nodes.
    # we also learned how to handle edge cases, such as inserting or deleting nodes at the beginning or end of the list,
    # and how to maintain the integrity of the list during these operations.
class LinkedList:
    def __init__(self):
        self.head = None
        #beginning of the LinkedList
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print("LinkedList is empty ")
            return
        
        itr = self.head
        llstr = ''
        
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
            
        print(llstr)
        
        #inserting a node at the end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
            
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None)
        #Here we are using none function in the head function which means we are deleting the existing LinkedList so that we can create a-
        #-new one altogether
    def insert_values(self, data_list):
            self.head = None
            for data in data_list:
                self.insert_at_end(data)
                
        #Finding the length of the LinkedList
    def get_length(self):
            count = 0
            itr = self.head
            while itr:
                count += 1
                itr = itr.next
                
            return count
        #Removing a node at a given index
    def remove_at(self, index):
            if index < 0 or index >= self.get_length():
                raise Exception("Invalid Index")
                
            if index == 0:
                self.head = self.head.next
                return
                
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    break
                    
                itr = itr.next
                count += 1
                
    #Inserting a node at a given index
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count += 1
            

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)  
    
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next
            
    def remove_by_value(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
    
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple")
    ll.print()
    ll.remove_by_value("orange")
    ll.print()
    ll.remove_by_value("banana")
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
    print("Length:", ll.get_length())
        