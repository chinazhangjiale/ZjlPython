import urllib.request
import os
response = urllib.request.urlopen("http://python.org/")
print(response.read())
