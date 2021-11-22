import urllib.request
urlPath = "https://www.python.org/static/img/python-logo.png"

urllib.request.urlretrieve(urlPath, "pyImage.png")