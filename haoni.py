def hanoi(n,x,y,z):#n盘子  x,y,z针
    if n==1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)#将前n-1个盘子从x移动到y上
        print(x,'-->',z)#将最后一个盘子移动到z上
        hanoi(n-1,y,x,z)#将y上的n-1个盘子移动到z上

n = int(input('汉诺一塔的层数'))
hanoi(n,'x','y','z')
