# importing requests package/media/savitha/01D3A025EB7EDBB0/Data Warehousing/web_scrapping/mongo.py
import requests
#from urllib3.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup as BS


def NewsFromNatGeo():
    main_url = " https://newsapi.org/v2/everything?sources=national-geographic&apiKey=95465951cbf447369c10a005ded49a0b"
    open_bbc_page = requests.get(main_url).json()
    article = open_bbc_page["articles"]
    browser = webdriver.PhantomJS()
    for ar in article:
        print("TITLE:",ar["title"])
        print("DATE:",ar['publishedAt'])
        print(ar["url"])
        try:
            browser.get(ar["url"])
            ans=''
            html = browser.page_source
            soup = BS(html, 'html.parser')
            table = soup.find_all('div',{'class':"parbase smartbody section text"})
            #k=''
            print(table)
            if len(table) >0:
                for i in table:
                    k=''
                    for jl in i.find_all('p'):
                        print(jl.string)
                        if jl.string!=None:
                            k = k+jl.string
                print(k)

        except:
            print("removing video articles")

# Driver Code
if __name__ == '__main__':
    # function call
    NewsFromNatGeo()
