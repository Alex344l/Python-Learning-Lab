class Myqueue:

    def __init__(self, cap):

        self.arr = [0] * cap

        self.capacity = cap

        self.top = -1

    def push(self, x):

        if self.top == self.capacity - 1:
            print("Queue  Overflow")
            return
        
        self.top += 1

        self.arr[self.top] = x

    def pop(self):

        if self.top == -1:
            print("Queue Underflow")
            return

        value = self.arr[0]

        for i in range(self.top):
            self.arr[i] = self.arr[i + 1]

        self.arr[self.top] = 0
        self.top -= 1
      

        return value

    def peek(self):

        if self.top == -1:
            print("Empty Stack")
            return -1
        
        return self.arr[0]


    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1


def find_max(arr):

    maximum = arr[0]

    for x in arr:
        if x > maximum:
            maximum = x

    return maximum

def find_duplicate(arr):

    duplicates = set()

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):

            if arr[i] == arr[j]:
                duplicates.add(arr[i])
                
            
    return duplicates


if __name__ == "__main__":

    q = Myqueue(10)

  


    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    q.push(6)
    q.push(7)
    q.push(8)
    q.push(3)
    q.push(7)

    
  


    
    print(q.arr)
    
    print("Popped: ", q.pop())

    print(q.arr)

    print("Popped: ", q.pop())

    q.push(8)
    q.push(9)

    print(q.arr)
    print("Peek: ", q.peek())

    maximum = find_max(q.arr)
    duplicate = find_duplicate(q.arr)

    print("Maximum: ", maximum)
    print("Duplicate: ", duplicate)