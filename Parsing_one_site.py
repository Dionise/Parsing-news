
from bs4 import BeautifulSoup
import urllib.request
info = urllib.request.urlopen('https://news.yam.md/')
html=info.read()
soup = BeautifulSoup(html, 'html.parser')
new=soup.find_all(class_="news-list-row story-row-container")
noutati =[]
for item in new:
    ora = item.find(class_="news-row-time").get_text()
    titlu = item.find(class_="news-row-title").get_text(strip=True)
    noutati.append(
         {
             'ora':ora,
             'titlu':titlu
         }
     )
print(noutati)
file=open('file.txt','w',encoding='UTF-8')
for itm in noutati:
   file.write(f'Ora: {itm["ora"]} titlu: {itm["titlu"]} \n\n')
file.close()
