import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    return html

def get_img(html):
    #r  源码转义 【^"】遇到"停 + 出现一次或多次
    p = r'<img src="([^"]+\.jpg)"'
    
    imag_list = re.findall(p, html)

    
    for each in imag_list:
        print(each)
    
    count =0
    for each in imag_list:
        count += 1
        if count > 6:
            file_name = each.split("/")[-1]
            urllib.request.urlretrieve(each, file_name, None)#urlretrieve自动下载这个地址

            
if __name__ == '__main__':
    url = 'http://blog.cuishuai.cc/meizi/page_8.html'
    get_img(open_url(url))
