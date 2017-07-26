from bs4 import BeautifulSoup

import requests

#url = "www.pythonforbeginners.com"
url = "www.moneycontrol.com"

# r  = requests.get("http://" +url)
r = requests.get("http://mmb.moneycontrol.com/forum-topics/latest-threads.html")
data = r.text

soup = BeautifulSoup(data)
p = soup.prettify(formatter=None).encode('utf-8')
print(p)
# for link in soup.find_all('a'):
#     print(link.get('href'))
#     