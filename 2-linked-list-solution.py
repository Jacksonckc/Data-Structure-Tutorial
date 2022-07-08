class Snake:
    def __init__(self):
        # Initialize an empty linked list.
        self.head = None
        self.tail = None


    class Section:
        def __init__(self, data):
            # Initialize the section to the data provided.  Initially
            # the links are unknown so they are set to None.
            self.data = data
            self.next = None
            self.prev = None
    
    def insert_head(self, color):
        new_section = Snake.Section(color)  
        
        if self.head is None:
            self.head = new_section
            self.tail = new_section

        else:
            new_section.next = self.head 
            self.head.prev = new_section 
            self.head = new_section   

    def remove_head(self):
        # Remove the first section (i.e. the head) of the linked list.
        if self.head == self.tail:
            self.head = None
            self.tail = None

        elif self.head is not None:
            self.head.next.prev = None  
            self.head = self.head.next  

    def insert_tail(self, color):
        new_section = Snake.Section(color)  

        if self.tail is None:
            self.head = new_section
            self.tail = new_section
        
        else:
            new_section.prev = self.tail
            self.tail.next = new_section
            self.tail = new_section
    
    def remove_tail(self):
        if self.tail == self.head:
            self.head = None
            self.tail = None
        elif self.tail is not None:
            self.tail.prev.next = None  
            self.tail = self.tail.prev 

    def remove_middle(self, color):
        current = self.head
        while current is not None:
            if current.data == color:
                if current.prev == None:
                    self.remove_head()
                elif current.next == None:
                    self.remove_tail()
                else:
                    current.prev.next = current.next 
                    current.next.prev = current.prev     
                # we don't need to return here once the first matching section is found, we continue the process until all the matching sections are deleted.
            current = current.next

    def show_snake_sections(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

snake = Snake()

food = [(0, 'red'),(0, 'red'),(0, 'orange'),(1, 'blue'),(2, 'red'),(0, 'red'),(1, 'yellow')]

for i in food:
    if i[0] == 0:

        snake.insert_head(i[1])
    elif i[0] == 1:
        snake.insert_tail(i[1])
    else:
        snake.remove_middle(i[1])


snake.show_snake_sections()
# red, orange, blue, yellow