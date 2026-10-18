class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "error"
        return self.items.pop(0)

    def front(self):
        if len(self.items) == 0:
            return "error"
        return self.items[0]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []


queue = Queue()

while True:
    command = input().split()

    if command[0] == "push":
        queue.push(int(command[1]))
        print("ok")

    elif command[0] == "pop":
        print(queue.pop())

    elif command[0] == "front":
        print(queue.front())

    elif command[0] == "size":
        print(queue.size())

    elif command[0] == "clear":
        queue.clear()
        print("ok")

    elif command[0] == "exit":
        print("bye")
        break