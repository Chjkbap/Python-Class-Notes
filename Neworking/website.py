import urllib.request

try:
    url = urllib.request.urlopen("https://www.python.org/")
    content = url.read()
    url.close()
except urllib.error.HTTPError:
    print("page not found")
    exit()
f  = open("python1.html", "wb") 
f.write(content)
f.close()