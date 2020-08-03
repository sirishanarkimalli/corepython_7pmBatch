import requests
from bs4 import BeautifulSoup

res= requests.get(f"http://rivr.sulekha.com/ravin_242574")

bs= BeautifulSoup(res.text,"html.parser")
s=set()
f= open(r"d:\ravibloglinks.txt","w")

for tag in bs.find_all('a'):
    try :
        if str(tag.attrs['href']).endswith("_blog"):
            link=tag.attrs['href']
            s.add(link)
            print(tag.attrs['href'])
    except KeyError as ke:
        pass

for line in s:
    if str(line).startswith("/"):
        f.write(line+"\n")
    else :
        f.write("/"+line+"\n")
f.close()