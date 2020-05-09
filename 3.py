def discount(price,rate):
    price = rate * price
    print('修改后的价格是:',price)
    

price = float(input('请输入初始价格'))
#折扣率
rate = 0.88
discount(price, rate)
print("打折后的价格:",price)



//效果同上
def discount2(*test):
    test[0] =  test[1] * test[0]
    print('修改后的价格是:',test[0])
    

price = float(input('请输入初始价格'))
#折扣率
rate = 0.88
discount(price, rate)
print("打折后的价格:",price)
