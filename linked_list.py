from node import Node
class LinkedList:
    def __init__(self):
        self.head = None
    def insertar_inicio(self,data):
        new_node= Node(data)
        new_node.next= self.head
        self.head= new_node
    def insertar_final(self,data):
        new_node= Node(data)
        if self.head is None:
            self.head=new_node
            return
        current= self.head
        while current.next is not None:
            current=current.next
        current.next=new_node
    def recorrer(self):
        current = self.head
        while current is not None:
            print(f"{current.data} ->", end=" ")
            current = current.next
        print("None")

    def buscar(self, obj):
        current = self.head
        while current is not None:
            if current.data == obj:
                return True
            current = current.next
        return False
    def ordenar(self):
        if self.head is None:
            return "la lista esta vacia"
        current = self.head
        while current.next is not None:
            index = current.next
            while index is not None:
                if current.data > index.data:
                    aux= current.data
                    current.data= index.data
                    index.data= aux
                index = index.next
            current = current.next
        def invertirLista(self,lista_enlazada):
            current = lista_enlazada.head
            prev = None 
            while current is not None:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            self.head = prev

