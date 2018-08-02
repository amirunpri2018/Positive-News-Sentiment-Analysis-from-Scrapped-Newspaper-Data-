import requests
from bs4 import BeautifulSoup as soup
url = "https://www.tripadvisor.com.sg/Attraction_Review-g294264-d2439664-Reviews-Universal_Studios_Singapore-Sentosa_Island.html"
def reviews_page(url):
    html_page = requests.get(url)
    soup_page = soup(html_page.content,"html.parser")
    containers = soup_page.findAll('div',{'class':'review-container'})
    for i in range(len(containers)):
        title = containers[i].find('span',{'class':'noQuotes'})
        location = containers[i].find('span',{'class':'userLocation'})
        review_text = containers[i].find('p',{'class':'partial_entry'})
        name = containers[i].find('div',{'class':'username mo'})
        rating = containers[i].find('span',{'class':'ui_bubble_rating'})    
        if not(location == None  or title == None):
            print(title.text)
            print(review_text.text)
            print(name.text)
            print(location.text)
            print(int(rating['class'][1].split("_")[1][0]))
def redirect(url):
    html_page = requests.get(url)
    soup_page = soup(html_page.content,"html.parser")
    page2 = soup_page.find('a',{'data-page-number':'3'})
    url2 = "https://www.tripadvisor.com.sg" +page2['href'] 
    print(url2)
    return url2

reviews_page(url)
url2 = redirect(url)
reviews_page(url2)
