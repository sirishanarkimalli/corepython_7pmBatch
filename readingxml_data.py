import requests
from bs4 import BeautifulSoup

resp= requests.get("http://charityapi.orghunter.com/rss.xml")

bs= BeautifulSoup(resp.text,"xml")

for tag in bs.find_all('item'):
    print(tag.title.text.strip())
    print(tag.link.text)
    print(tag.pubDate.text[0:17])
    print()







