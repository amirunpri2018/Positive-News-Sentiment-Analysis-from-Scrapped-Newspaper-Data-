import re
from selenium import webdriver
from bs4 import BeautifulSoup as BS

url = 'https://www.straitstimes.com'
#pjs = r'E:/ISBA/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/'
# pjs = 'C:\Python36-32\phantomjs-2.1.1-windows\bin\phantomjs.exe' #desktop
#webdriver.add_argument("--headless")
browser = webdriver.PhantomJS()
browser.get(url)
html = browser.page_source
soup = BS(html,'html.parser') #note that it is not html.content
table = soup.find_all('a',{'class':"block-link", 'href':True})
print(table)
for i in table:
#print(i['href'])
    if "javascript" not in i['href'] and len(i['href'])>0 and not "https" in i['href']:
        k=url+str(i['href'])
        print(k)
        browser.get(k)
        html=browser.page_source
        soup=BS(html,'html.parser')
        title_article=soup.find('h1',{'class':re.compile("headline")})
        print(title_article.string,"is the title of the article")
        table = soup.find_all('div',{'class':'odd field-item'})[0].find_all('p')
        j=0
        k=''
for i in table:
    if i.string!=None and not 'TO READ THE FULL ARTICLE' in i.string:
        k = k+str(i.string)
    else:
        j=j+1
if j>1:
            print("login is required")
else:
            print(k)
        else:
            next
            #print(table)
browser.quit()
