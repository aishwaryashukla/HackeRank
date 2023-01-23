from bs4 import BeautifulSoup
import urllib
import re


url = "https://github.com/search?q=sumit&type=Users"

content = urllib.request.urlopen(url)

soup = BeautifulSoup(content, "lxml")
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print(link.get('href'))

#print soup.prettify()

#print (soup.find_all('li').get_text())
#for tag in soup.find_all(re.compile(r"([\w\.\-_]+)?\w+@[\w-_]+(\.\w+){1,}")):
#    print(tag)
#mydivs = soup.findAll("div", {"class": "stylelistrow"})

lis = soup.find_all('div', {"class": "d-block d-md-inline f4 mt-2 mt-md-0 ml-md-1"})
lis2 = soup.find_all('p', {"class": "f5 mt-2"})
list2 = ""

##Getting Names
for list in lis:
    print(list.get_text())

##Getting All Links
#for link in soup.find_all('a', href=True):
#    print(link['href'])