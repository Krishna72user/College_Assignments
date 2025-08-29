class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        ptr = Node(data)
        if not self.head:
            self.head = ptr
            return
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = ptr
    
    def delete_from_beg(self):
        if self.head is None:
            print("List is already empty")
            return
        self.head = self.head.next
        
    def traversal(self):
        ptr = self.head
        if not ptr:
            print("List is already empty")
            return
        while ptr != None:
            print(ptr.data, end=" ")
            ptr = ptr.next
        print()

lst = LinkList()
lst.insert(10)
lst.insert(20)
lst.insert(30)

print("Original List:")
lst.traverse()

lst.delete_from_beginning()

print("After deleting first node:")
lst.traverse()