import requests
from bs4 import BeautifulSoup

url="https://codewithharry.com"
req=requests.get(url)
result=req.content

Beaut=BeautifulSoup(result,'html.parser')

para=Beaut.find_all('p')
print(para)

anchore=Beaut.find_all('a')
print(anchore)