def invertirLista(self,lista_enlazada):
    current = lista_enlazada.head
    prev = None 

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    self.head = prev

    






    