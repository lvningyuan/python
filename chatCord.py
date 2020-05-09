f = open("chatCord.txt",encoding='utf-8')

boy  = []
girl = []
count = 1

for each_line in f:
    if  each_line[0:3] != '===':
        (role, spoken) = each_line.split(':',1)
        if role == '空荡':
            boy.append(spoken)
        if role == '虚无':
            girl.append(spoken)
    else:
        boy_file_name = 'boy'+  str(count) + '.txt'
        girl_file_name = 'girl' + str(count) + '.txt'

        boy_file = open(boy_file_name, 'w',encoding='utf-8')
        girl_file = open(girl_file_name, 'w',encoding='utf-8')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        count += 1
        boy = []
        girl = []
f.close()
