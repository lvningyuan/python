import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/400/400")
cat_image = response.read()

with open('cat_400*400.jpg','wb') as f:
    f.write(cat_image)
