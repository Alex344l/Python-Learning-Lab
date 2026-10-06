class myQueue:

    def __init__(self, cap):

        self.arr = [0] * cap
        self.capacity = cap
        self.top = -1


    def enqueue(self, x):

        if self.top == self.capacity - 1:
            print("Queue Overflow")
            return

        self.top += 1

        self.arr[self.top] = x


    def dequeue(self):

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
            print("Queue is empty")
            return
        
        return self.arr[0]



class Mystack:

    def __init__(self, cap):

        self.arr = [0] * cap

        self.capacity = cap

        self.top = -1

    def push(self, x):

        if self.top == self.capacity - 1:
            print("Stack Overflow")
            return
        
        self.top += 1

        self.arr[self.top] = x

    def pop(self):

        if self.top == -1:
            print("Stack Underflow")
            return

        value = self.arr[self.top]
        self.arr[self.top] = 0
        self.top -= 1
      

        return value

    def peek(self):

        if self.top == -1:
            print("Empty Stack")
            return -1
        
        return self.arr[self.top]


def rm_duplicates(arr):

    seen = set()
    result = []

    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)

    return result




if __name__ == "__main__":

    q  = myQueue(15)
    st = Mystack(15)

    

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)
    q.enqueue(10)


    while q.top != -1:

        value = q.dequeue()
        st.push(value)

    while st.top != -1:

        value = st.pop()
        q.enqueue(value)

    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    rm_duplicates = rm_duplicates(q.arr)

    q.dequeue()

    print(q.arr)

    
    print("No duplicates: ", rm_duplicates)

    