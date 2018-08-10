# 单链表元素
class SingleLinkList():
    def __init__(self, data, nextL=None):
        self.data = data
        self.next = nextL

    def __getitem__(self, key):
        def LinkRead(linklist, i=1):
            if isinstance(linklist, SingleLinkList):
                sll = linklist
                # 如果查找的不是第一个
                for j in range(0, i):
                    if j < i and sll.next is None:
                        return False
                    sll = sll.next
                return sll.data
            else:
                return False
        return LinkRead(self, key)


# 创建单链表
def CreatList(n=1): 
    # 创建头结点
    llhead = SingleLinkList('head')
    sll = llhead
    for i in range(0, n):
        newLL = SingleLinkList(i+1)
        sll.next = newLL
        sll = sll.next
    return llhead


# 单链表的读取
def LinkRead(linklist, i=1):
    if isinstance(linklist, SingleLinkList):
        sll = linklist
        # 如果查找的不是第一个
        for j in range(0, i):
            if j < i and sll.next is None:
                return False
            sll = sll.next
        return sll.data
    else:
        return False


# 单链表的插入
def LinkInsert(linklist, i, data):
    if isinstance(linklist, SingleLinkList):
        sll = linklist
        for j in range(0, i-1):
            sll = sll.next
            if j < i-2 and sll.next is None:
                return False  
        node = SingleLinkList(data)
        node.next = sll.next
        sll.next = node
        return linklist
    else:
        return False


# 单链表的删除
def LinkDelet(linklist, i):
    if isinstance(linklist, SingleLinkList):
        sll = linklist
        for j in range(0, i-1):
            sll = sll.next
            if sll.next is None:
                return linklist
        sll.next = sll.next.next
        return True
    else:
        return False
#test
if __name__ == '__main__':
    ll = CreatList(10)
    a = ll
    LinkDelet(a, 4)
    for i in range(11):
        print(ll[i])
      
