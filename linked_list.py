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

    def eliminar_inicio(self):
        if self.head is None:
            return "La lista está vacía"
        self.head = self.head.next
        return None

    def eliminar_por_valor(self, valor):
        if self.head is None:
            return "La lista está vacía"
        
        if self.head.data == valor:
            self.head = self.head.next
            return None
        
        current = self.head
        while current.next is not None:
            if current.next.data == valor:
                current.next = current.next.next
                return None
            current = current.next
        
        return "El valor no se encuentra en la lista"
    
    def ordenamiento(self):
        swapped = True

        while swapped:
            swapped = False
            current = self.head
            prev = None

            while current is not None and current.next is not None:
                if current.data > current.next.data:
                    next_node = current.next
                    swapped = True

                    current.next = next_node.next
                    next_node.next = current

                    if prev is None:
                        self.head = next_node
                    else:
                        prev.next = next_node

                    prev = next_node
                else:
                    prev = current
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
    def tamañoLista(self,lista_enlazada):
            current = lista_enlazada.head
            contador = 0
            while current is not None:
                contador +=1
                current = current.next
            return contador


