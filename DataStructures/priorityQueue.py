# Implementing Prirotiy Queue

class PriorityQueue(object):

    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert(self, data):
        self.queue.append(data)

    def delete(self):

        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            
            item = self.queue[max]
            del self.queue[max]
            return item

        except IndexError:
            print()
            exit()

if __name__=="__main__":

    print("Creating and Adding to Priority Queue: ")
    q = PriorityQueue()
    q.insert(10)
    q.insert(12)
    q.insert(42)
    q.insert(22)
    q.insert(17)
    print(q)

    print("\nPopping from the Priority Queue: ")
    while not q.isEmpty():
        print(q.delete())
