import calendar
import os
from bs4 import BeautifulSoup
import urllib.request
response = urllib.request.urlopen("http://python.org/")
soup = BeautifulSoup(response)
#print(soup.prettify())
p = soup.prettify(formatter=None).encode('utf-8')
print(p)