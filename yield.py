def generator():
    a = 0
    b = 1
    print("开始迭代生成器")
    while True:
        a,b = b, a+b
        yield a

for each in generator():
    if(each > 100):
        break
    print(each,end = ' ')#不换行 ，以空格代替换行
