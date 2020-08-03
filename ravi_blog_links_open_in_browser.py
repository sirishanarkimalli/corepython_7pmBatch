from idlelib.searchengine import get

import requests
from bs4 import BeautifulSoup
import webbrowser

def getContent():
    with open(r"d:\ravibloglinks.txt") as f:
        for line in f:
            link="http://creative.sulekha.com"+line.strip()
            resp= requests.get(link)
            bs=BeautifulSoup(resp.text,"html.parser")
            with open(r"d:\blogContent.txt","a") as f1:
                f1.write(line.upper()+"\n")
                print(link)
                for t in bs.find_all('p'):
                    for lines in t.text:
                        f1.write(lines)
    f1.close()
    f.close()
def openlinks():
    with open(r"d:\ravibloglinks.txt") as f:
        for line in f:
        # link="https://google.com/search?="+str(line)
        # resp= requests.get()
        # bs=BeautifulSoup(resp.text,"html.parser")
            webbrowser.open("http://creative.sulekha.com"+str(line))

# Read links from file and opens in browser
# openlinks()
getContent()