class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]#列表推导式 
        self.count = {}.fromkeys(range(len(self.values)),0)#建立字典记录访问次数

    #字典；0 - len(self.value) 
    def __len__(self):
        return len(self.values)

    #获取值， 并不是获取访问次数
    #gwtitem ,只要访问 必定触发， 这就是魔法
    def __getitem__(self,key):
        self.count[key] +=1
        return self.values[key]
