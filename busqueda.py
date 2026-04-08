def search(self, target):
    current = self.head

    while current is not None:
        if current.data == target:
            return True
        current = current.next

    return False