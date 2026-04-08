from node import Node
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    
    def show(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("null")

   
    def delete_start(self):
        if self.head is None:
            print("La lista está vacía")
            return

        self.head = self.head.next

    
    def delete_value(self, value):
        if self.head is None:
            print("La lista está vacía")
            return

       
        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

        print("Valor no encontrado")