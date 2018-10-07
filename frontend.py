from tkinter import *
#import mongo
import backend
import pymongo
from pymongo import MongoClient

c = MongoClient()
db=c["mydatabase"]
article = db.articles

def view_command():
    #list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
"""
def search_command():
    list1.delete(0,END)
    for post in tw.find({field: regx},{'score':5},limit=30):
        list1.insert(END,row)
"""
window=Tk()

window.wm_title("PosNews")

"""
l1=Label(window,text="Title")
l1.grid(row=0,column=0)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

"""
list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#list1.bind('<<ListboxSelect>>',get_selected_row)


b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=2,column=3)


window.mainloop()
