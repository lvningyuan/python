class Rectangle:
    def __init__(self,width =0, height = 0):
        self.width = width
        self.height = height
    def __setattr__(self, name, value):#原理 ：1 修改 2 不存在 再来创建属性
        if name == 'square':            #对象访问a.name = value    
            self.width = value
            self.height = value
        else:
            #不要这样写，会引起死循环。   self.name = value

            #这样是正确的:
            super().__setattr__(name, value)
            #这样也可以：原理是底层实际上是建立字典的
            #self.__dict__[name] = value
            
    def getArea(self):
        return self.height * self.width
