import requests
from bs4 import BeautifulSoup
import shutil

def fetchimage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0'
        
    }
    r  = requests.get(url,headers=headers)
    html=r.text
    soup=BeautifulSoup(html)
    comic=soup.find("div", class_="comicpane")
    return comic.img['src']


def download(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0'
        
    }        
    response = requests.get(url, stream=True,headers=headers)
    with open(url.split('/')[-1], 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response


url='http://zenpencils.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0'
    
}
r  = requests.get(url,headers=headers)
html=r.text
soup=BeautifulSoup(html)
res=soup.find_all('option')
mastertable=[]
for op in reversed(res[1:]):
    mastertable.append((op.contents[0],op['value'])) 
c=1
for entry in mastertable:
    url=entry[1]
    title=entry[0]
    comic=fetchimage(url)
    download(comic)
    print "dloaded ",c
    c+=1

