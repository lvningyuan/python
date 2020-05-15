import urllib.request
import urllib.parse

url = "http://rlogs.youdao.com/rlog.php?_npid=fanyiweb&_ncat=event&_ncoo=140048614.65942466&_nssn=NULL&_nver=1.2.0&_ntms=1588563729245&_nhrf=first-touch&keyfrom=fanyi.logo"


#...
#方式一  前期添加
#head ={}
#head['User-Agent'] = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36"
#...


data ={}
data['i'] = '蜘蛛'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult']= 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15885582446783'
data['sign'] = 'd3895f1f2d97daa4fe8478fb32bdbd71'
data['ts'] = '1588558244678'
data['bv'] ='8cf0b66b969dff5f3b932c0e257cf42d'
data['doctype']= 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'lan-select'
data = urllib.parse.urlencode(data).encode('utf-8')   #  转化为unicode  中的utf-8

#
response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8') # utf-8 ---> unicode
print(html)
