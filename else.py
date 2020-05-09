def S(x):
    count = x // 2
    while count > 1:
        if x % count == 0:
            print('%d的最大约数%d: '% (x, count))
            break 
        count -= 1
    else:
        print('%d是素数'% x)

#x = int(input("请输入一个数"))
#S(x)


try :
    a =3
 #   print(a / 0)
    print(a > 0)
except ZeroDivisionError as reason:
    print("出错啦，原因是：",str(reason))
else:
    print("没有任何异常！")


try:
    with open('data.txt') as f
    for each_line in f:
        print(each_line)
except OSError as reason:
    print("出错原因：" + str(reason))
#finally:
#   f.close()
