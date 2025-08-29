class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)
        return
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            val = self.items.pop(0)
            return val
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.items[0]
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            for item in self.items:
                print(item, end=" ")

q1 = Queue()
q2 = Queue()

print("\n----- Stack Menu -----")
print("1. Push")
print("2. Pop")
print("3. Peek")
print("4. Display")
print("5. Exit")

while True:
    choice = int(input("\nChoose your option: "))
    
    match choice:
        case 1:
            data = int(input("Enter the element: "))
            if q1.is_empty():
                q1.push(data)
            else:
                while not q1.is_empty():
                    q2.push(q1.pop())
                q1.push(data)
                while not q2.is_empty():
                    q1.push(q2.pop())
            
        case 2:
            val = q1.pop()
            print(val)
            
        case 3:
            val = q1.peek()
            print(val)
            
        case 4:
            q1.display()
            print()
            
        case 5:
            print("Exiting.....")
            break
            
        case _:
            print("\nInvalid choice!")
            