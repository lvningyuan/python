import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/1300/1800")
html = response.read()

with open('miao4.jpg','wb') as f:
    f.write(html)

