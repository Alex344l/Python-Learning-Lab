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


    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1




if __name__ == "__main__":

    st = Mystack(10)


    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)
    st.push(6)
    st.push(7)
    st.push(8)


    
    print(st.arr)
    
    print("Popped: ", st.pop())

    print(st.arr)

    print("Popped: ", st.pop())

    print(st.arr)


