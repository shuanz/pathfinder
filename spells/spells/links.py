import requests
from bs4 import BeautifulSoup

URL = "https://pf2srd.com.br/magias"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
f = open("spells_link.txt", "a")
for a in soup.find_all('a', href=True):
    print(a['href'])
    f.write(a['href']+'\n')
f.close()