import urllib.request
import random

url = "http://www.whatismyip.com.tw"#一个测试当前IP的网站

iplist =['122.200.90.11:53095','125.123.152.159:3000','183.166.253.96:4216','115.206.100.87:8060', '117.114.149.66:53281', '114.216.50.188:8118', '211.142.169.4:808']

#创建字典 ip + port

proxy_support  =  urllib.request.ProxyHandler({'http':random.choice(iplist)});


# build_opener

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36(KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36')]

# install_opener

urllib.request.install_opener(opener)


# use


#install 将 opener安装在了 request内
response  = urllib.request.urlopen(url) 
#response = opener.open(url)
html = response.read().decode('utf-8')

print(html)

