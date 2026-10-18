class Deque:
    def __init__(self):
        self.items = []

    def push_front(self, item):
        self.items.insert(0, item)

    def push_back(self, item):
        self.items.append(item)

    def pop_front(self):
        if len(self.items) == 0:
            return "error"
        return self.items.pop(0)

    def pop_back(self):
        if len(self.items) == 0:
            return "error"
        return self.items.pop()

    def front(self):
        if len(self.items) == 0:
            return "error"
        return self.items[0]

    def back(self):
        if len(self.items) == 0:
            return "error"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []


deque = Deque()

while True:
    command = input().split()

    if command[0] == "push_front":
        deque.push_front(int(command[1]))
        print("ok")

    elif command[0] == "push_back":
        deque.push_back(int(command[1]))
        print("ok")

    elif command[0] == "pop_front":
        print(deque.pop_front())

    elif command[0] == "pop_back":
        print(deque.pop_back())

    elif command[0] == "front":
        print(deque.front())

    elif command[0] == "back":
        print(deque.back())

    elif command[0] == "size":
        print(deque.size())

    elif command[0] == "clear":
        deque.clear()
        print("ok")

    elif command[0] == "exit":
        print("bye")
        break