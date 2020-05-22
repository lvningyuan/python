import urllib.request
import os

def open_url(url):
    ret = urllib.request.Request(url)
    ret.add_header('User-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36')
    response = urllib.request.urlopen(ret)
    html = response.read()

    return html;


def find_image(url):
    html = open_url(url).decode('utf-8')
    image_addrs =[]


    a = html.find('img src="')
    while a != -1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
            image_addrs.append(html[a+9:b+4])
        else:
            b = a + 9
        a = html.find('img src=',b) 

    for each in image_addrs:
        print(each)

    return image_addrs
    
    
    


def save_image(addr):
    for each in addr:
        #html = url_open(each)
        filename = each.split('/')[-1]
        print(filename)
        with open(filename,'wb') as f:
            image = open_url(each)
            f.write(image)
    
    

def download_mm(folder='mms',page=100):
    #url = 'http://www.crcz.com/touxiang/nv/2019/4417.html'

    os.mkdir(folder)
    os.chdir(folder)

    j=4193
    for i in range(page):
        url= 'http://www.crcz.com/touxiang/nv/2019/' + str(j) +'.html'
        j += 1

        #open_url(url)
        image_addrs = find_image(url)
        save_image(image_addrs)



if __name__ =='__main__':
    download_mm()
