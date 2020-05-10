try:
    f = open("hahahaha.txt")
    print(f.read())
    f.close()
#except:
#   print('出错了') 这样不太好
except OSError as reason:
    print('出错了,原因是;',str(reason));
except TypeError as reason:
    print('出错了,原因是;',str(reason));
