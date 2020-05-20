import urllib.request
import os

#http://blog.cuishuai.cc/meizi/page_4.html


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    return html


#获取所在页
def get_page(url):
    html = open_url(url).decode()
    
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)

    print(a)
    print(b)
    print(html[a:b])
    return html[a:b]


#/<img src="/upload/article/201807/06/0950225b3ecadeb5a8flqnJnM_thumb.jpg">
#寻找图片
def find_imag(url):
    html = open_url(url).decode('utf-8')
    imag_addrs =[] #存放找到图片的地址
    
    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg',a, a+255)
        
        if b != -1:
            imag_addrs.append(html[a+9:b+4]) #找到了 ，保存图片地址
        else:
            b = a + 9 # 从a+9处开始从新找
            
        a = html.find('img src',b)
    for i in imag_addrs:
        print(i)
    return imag_addrs
     


#保存图片
def save_imag(folder,imag_addr):
    count =0;
    for each in imag_addr:
        count += 1
        if count > 6:
            filename = each.split('/')[-1] #最后一个/后的就是文件名
            print(filename)
            with open(filename, 'wb') as f:
                imag = open_url(each) #打开每张图片,获得二进制数据
                f.write(imag)         #将图片写入文件


#准备下载
def download_mm(folder ='ooxx', pages =10):
    os.mkdir(folder)
    os.chdir(folder)

    url= 'http://blog.cuishuai.cc/meizi/'
    #page_num = int (get_page(url))
    open_url(url)
    for i in range(pages):
        #page_num -= i
        page_url = url + 'page_' + str(i) + '.html'#拼成链接
        imag_addr = find_imag(page_url)#打开链接找到图片
        save_imag(folder, imag_addr)
             
        
if __name__ == '__main__':
    download_mm()
