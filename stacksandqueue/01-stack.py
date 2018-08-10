# 栈元素
class StackEle(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    pass


# 栈类
class Stacks(object):
    # 初始化
    def __init__(self, n=0):
        self.__len = n
        self.__head = None
        for i in range(0,n):
            newSTE = StackEle(i)
            newSTE.next = self.__head
            self.__head = newSTE
    # 清空栈
    def clear(self):
        self.__head = None
        self.__len = 0
        return True

    # 判断栈是否为空
    def isEmpty(self):
        if self.__head is None:
            return True
        else:
            return False
    # 压入栈
    def push(self,e):
        newSTE = StackEle(e)
        newSTE.next = self.__head
        self.__head = newSTE
        self.__len +=1
        return True
    # 弹出
    def pop(self):
        if self.isEmpty():
            return False
        else:
            self.__len -=1
            topE = self.__head
            self.__head = topE.next
            topE.next = None
            return topE.data
    # 获取栈顶的值
    def getTop(self):
        if self.isEmpty():
            return False
        else:
            return self.__head.data
    # 返回栈的元素个数
    def len(self):
        return self.__len

# test
if __name__ == '__main__':
    stk = Stacks()
    print('stk is empty : %s' % stk.isEmpty())
    stk.push('first')
    print('stk length is %s' % stk.len())
    print(stk.pop())
    print('stk length is %s' % stk.len())
    stk.clear()
    print('stk length is %s' % stk.len())

