##########
# 队列节点
class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next =next
# 队列
class Queue(object):
    # 初始化
    def __init__(self, n=0):
        headNode = Node('head')
        self.__head = headNode
        self.__tail = self.__head
        self.__len = n
        for i in range(0, n):
            newNode = Node(i)
            self.__tail.next = newNode
            self.__tail = self.__tail.next
    # 清空队列
    def clear(self):
        self.__head.next = None
        self.__tail = self.__head
        self.__len = 0
    # 判断是否为空
    def isEmpty(self):
        return self.__tail is self.__head
    # 插入元素到队尾
    def put(self,e):
        newNode = Node(e)
        self.__tail.next = newNode
        self.__tail = self.__tail.next
        self.__len +=1
        return True
    # 从队首获取元素并删除
    def get(self):
        if self.isEmpty():
            return False
        else:
            firstNodedata = self.__head.next.data
            self.__head = self.__head.next
            self.__head.data = 'head'
            self.__len -= 1
            return firstNodedata
    # 获取队列长度
    def len(self):
        return self.__len
# test
if __name__ == '__main__':
    q = Queue(100)
    for i in range(100):
        print(q.get())  
    print('q length is %d '% q.len())
    print('q get a ele: %s'% q.get())
    print('q is empty : %s' % q.isEmpty())
    print('q put a ele: %s' % q.put('hh'))
    q.clear()
    print('q get a ele: %s' % q.get())
    print('q is empty : %s' % q.isEmpty())
    
