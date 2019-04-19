import heapq
# 优先队列类
class PriorityQueue:
    def __init__(self):
        self._queue=[]
        self._index=0
    
    def push(self,item,priority):
        heapq.heappush(self._queue,(priority,self._index,item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
# 队列元素类
class Item:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)



q=PriorityQueue()
n=input("请输入元素个数:\n")
n=int(n)
for i in range(n):
    name=str(input("请输入元素名称:\n"))
    prio=int(input("请输入优先值\n"))
    q.push(Item(name),prio)
for i in range(n):
    print(q.pop())
    