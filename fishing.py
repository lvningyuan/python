print("我爱钓鱼  工作室")

temp = input("猜猜小甲鱼喜欢吃哪个编号的鱼饵")

guess = int(temp)
if guess == 8:
    print("卧槽，上钩了")
    print('哼，猜中也没奖励！')
else:
    print('猜错啦，小甲鱼的菜是 8 号')
print('You  lose the  game,  game over!')
