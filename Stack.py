class StackException(ValueError):
    def __init__(self, ex, mess):
        self.ex = ex
        self.mess = mess
class Stack:
    def __init__(self):
        self.Stack = []
        self.size = 0
    def clear(self):
        self.Stack.clear()
        self.size = 0
    def contains(self, values):
        for item in self.Stack:
            if(item is values):
                return True
        return False
    def peek(self):
        if (self.isEmpty()):
            raise StackException('Stack Error','Stack  cannot peek')
        return self.Stack[self.size-1]
    def push(self,value):
        
        self.Stack.append(value)
        self.size+=1
    def pop(self):
        if (self.isEmpty()):
            raise StackException('Stack Error','Stack cannot pop')
        self.size-=1
        return self.Stack.pop(self.size)
    def isEmpty(self):
        return self.size<1
