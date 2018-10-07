# importing requests package/media/savitha/01D3A025EB7EDBB0/Data Warehousing/web_scrapping/mongo.py
import requests
#from urllib3.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup as BS


def NewsFromMirror():
    main_url = "https://newsapi.org/v2/top-headlines?sources=mirror&apiKey=3bb3d817cfe14cc0b52e0b2984a6ad99"
    open_bbc_page = requests.get(main_url).json()
    article = open_bbc_page["articles"]
    browser = webdriver.PhantomJS()
    for ar in article:
        print("TITLE:",ar["title"])
        print("DATE:",ar['publishedAt'])
        try:
            browser.get(ar["url"])
            ans=''
            html = browser.page_source
            soup = BS(html, 'html.parser')
            table = soup.find('div',{'class':"article-body"}).find_all('p')
            #print(table)
            for t in table:
                print(t.string)
                if t.string is not None:
                    ans=ans+t.string
            print(ans)
        except:
            print("removing video articles")

# Driver Code
if __name__ == '__main__':    # function callNewsFromNatGeo()
    NewsFromMirror()
