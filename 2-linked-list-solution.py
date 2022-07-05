class LinkedList:
    def __init__(self):
        # Initialize an empty linked list.
        self.head = None
        self.tail = None


    class Node:
        def __init__(self, data):
            # Initialize the node to the data provided.  Initially
            # the links are unknown so they are set to None.
            self.data = data
            self.next = None
            self.prev = None
    
    def employee_insertion(self, name):
        new_node = LinkedList.Node(name)  
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node   

    def remove_head(self):
        # Remove the first node (i.e. the head) of the linked list.
        if self.head == self.tail:
            self.head = None
            self.tail = None

        elif self.head is not None:
            self.head.next.prev = None  
            self.head = self.head.next  

    def customer_insertion(self, name):
        new_node = LinkedList.Node(name)  

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def remove_tail(self):
        if self.tail == self.head:
            self.head = None
            self.tail = None
        elif self.tail is not None:
            self.tail.prev.next = None  
            self.tail = self.tail.prev 

    def customer_with_fam_or_friend_insertion(self, friend_or_fam_name ,name):
        new_node = LinkedList.Node(name)  

        current = self.head
        while current is not None:
            if current.data == friend_or_fam_name:
                if current == self.tail:
                    self.insert_tail(name)
                else:
                    new_node.prev = current
                    new_node.next = current.next
                    current.next.prev = new_node
                    current.next = new_node
                return
            
            current = current.next

    def remove_customer_from_line(self, name):
        current = self.head
        while current is not None:
            if current.data == name:
                if current.prev == None:
                    self.remove_head()
                elif current.next == None:
                    self.remove_tail()
                else:
                    current.prev.next = current.next 
                    current.next.prev = current.prev  
                return             
            current = current.next

    def all_customer_names(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

list = LinkedList()

list.customer_insertion("Jackson")
# The Line: Jackson

list.employee_insertion("Talia")
# The Line: Talia, Jackson

list.customer_insertion("Bob")
# The Line: Talia, Jackson, Bob

list.customer_insertion("James")
# The Line: Talia, Jackson, Bob, James

list.customer_insertion("Eric")
# The Line: Talia, Jackson, Bob, James, Eric

list.customer_with_fam_or_friend_insertion("Jackson", "David")
# The Line: Talia, Jackson, David, Bob, James, Eric

list.remove_customer_from_line('James')
# The Line: Talia, Jackson, David, Bob, Eric

list.all_customer_names()