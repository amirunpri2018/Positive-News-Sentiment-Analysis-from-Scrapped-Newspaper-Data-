import pymongo
from pymongo import MongoClient
import requests
#from urllib3.request import urlopen
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import re

c = MongoClient()
db=c["mydatabase"]
article = db.articles

def insertIntoDB(date,title, content, source, url):
	post_Data ={'date': date, 'title':title,'content':content,'source':source,'url':url,'score':'NA'}
	result = article.insert_one(post_Data)

def updateScore():
	article.find({'score':'NA'})

#insertIntoDB('18/8/2018','Hi','Gen','Hello','bbc','www')
#updateScore()

def newsFromGuardian():
    main_url = "https://newsapi.org/v2/everything?sources=the-guardian-uk&apiKey=fa6d77b861bc48c2a4bfd93ef6ceaeba"

    # fetching data in json format
    open_bbc_page = requests.get(main_url).json()
    print(open_bbc_page)
    print(len(open_bbc_page),"is the length of the json return")


    article = open_bbc_page["articles"]


    results = []
    links = []
    url = []
    answer = []
    title_ret=[]
    time_art=[]
    browser = webdriver.PhantomJS()

    for ar in article:
        print(ar["title"])
        print(ar["url"]) #url
        print(ar['publishedAt'])#time
        print("the-guardian-uk")#source
        browser.get(ar["url"])
        #links.append(ar["url"])
        #title_ret.append(ar["title"])
        #time_art.append(ar['publishedAt'])

        ans=''

        html = browser.page_source
        soup = BS(html, 'html.parser')
        table = soup.find('div',{'class':re.compile('content__article-body')}).find_all('p')
        #print(table)
        for k in table:
            if k.string is not None:
                ans=ans+k.string
                #print(k.string)
        #answer.append(ans)
        print(ans) #article
        insertIntoDB(ar['publishedAt'],ar["title"], ans, "the-guardian-uk", ar["url"])
    #print(answer,links,title_ret,time_art)

newsFromGuardian()
