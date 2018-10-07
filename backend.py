#import mongo
import pymongo
from pymongo import MongoClient

def view():
    c = MongoClient()
    db=c["mydatabase"]
    article = db.articles
    #for post in article.find_on('score':)
    document = article.find_one()
    return document

view()
#insert("The Sun","John Smith",1918,913123132)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(author="John Smooth"))
