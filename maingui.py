import tkinter as tk
from tkinter import filedialog, Text
import os
from tkinter.constants import X
from PIL import Image, ImageTk

from bs4 import BeautifulSoup
import requests
import re
import urllib.request
import numpy as np

import pandas as pd
from pandas import DataFrame

root = tk.Tk()
root.title("G LUONG'S WIKIPEDIA IMAGE AND TABLE SCRAPER!")


def input_img_scrape():

    test_path = E1.get()
    url = E2.get()
    n_images = int(E3.get())
    if(E4.get() != ''):
        os.chdir(E4.get())  

    try:
        os.mkdir(test_path)

    except OSError:
        current_path = os.getcwd() + '\\' + test_path
    else:
        print ("successfully created the directory %s " % test_path)
        current_path = os.getcwd()

    html_content = requests.get(url, allow_redirects=True).text
    soup = BeautifulSoup(html_content, 'lxml')

    bs4 = soup.findAll('img', limit=n_images)

    def formaturl(url):
        if not re.match('(?:http|ftp|https):', url):
            return 'http:{}'.format(url)
        return url

    urlArr = []

    def removing_characters(str):
        regex = "[a-z, \s, ()]"
        return (re.sub(regex, "", str))

    for tag in bs4:
        url = tag['src']
        name = tag['alt']
        newurl = formaturl(url)
        urlArr.append(newurl)


    def urlarray(urlx):
        for i, urlx in enumerate(urlArr):
            save_name = os.path.join(test_path, f'{test_path}_{i}.jpg')
            urllib.request.urlretrieve(urlx, save_name)
        return urlx
    
    L4b.config(text='saved images at ' + os.sep.join(os.path.normpath(current_path).split(os.sep)[-3:]))

    urlarray(urlArr)

#END OF IMG SCRAPE FUNCTION

def input_table_scrape():
    name = E5.get()
    url = E6.get()
    if(E7.get() != ''):
        os.chdir(E7.get())     

    if(name or url == ''):
          L4b.config(text="you haven't input any data")    


    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, 'lxml')

    ctr_table = soup.findAll('table', class_='wikitable', limit= 3)
    dflist = pd.read_html(str(ctr_table))
    df = pd.DataFrame(dflist[0])
    #print(df.head(10))
    if(var.get() == 0):
       df.to_csv(f'{name}.csv')
    if(var.get() == 1):
       df.to_json(f'{name}.json', orient="split")
    if(var.get() == 2):
        df.to_html(f'{name}.html')

    L4b.config(text='saved table at ' + os.sep.join(os.path.normpath(os.getcwd()).split(os.sep)[-3:]))

def clr_img_scrape():
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    E3.delete(0, 'end')

def clr_table_scrape():
    E5.delete(0, 'end')
    E6.delete(0, 'end')
    E7.delete(0, 'end')

def handle_click(event):
    print("clicked!")

root.iconbitmap('favicon.ico')

bg_img = tk.PhotoImage(file="bg-img.png")
imglabel = tk.Label(root, image=bg_img)
imglabel.pack()

root.minsize(800, 500)
root.maxsize(1000, 600)

ImgLabel = tk.Label(root, text="IMAGE SCRAPER")
ImgLabel.place(width=145, height=20, relx=0.5, rely=.05)

L1 = tk.Label(root, borderwidth=2, relief='sunken', text="enter name for local folder")
L1.place(width=160, height=20, relx=0.08, rely=.1)
E1 = tk.Entry(root, bd =2)
E1.place (relwidth=0.45, height=20, relx=0.35, rely=.1)


L2 = tk.Label(root, borderwidth=2, relief='sunken', text="enter wikipedia url here")
L2.place(width=160, height=20, relx=0.08, rely=.15)
E2 = tk.Entry(root, bd =2)
E2.place (relwidth=0.45, height=20, relx=0.35, rely=.15)

E2.bind("<1>", handle_click)

L3 = tk.Label(root, borderwidth=2, relief='sunken', text="how many images you want")
L3.place(width=160, height=20, relx=0.08, rely=.2)
E3 = tk.Entry(root, bd =2)
E3.place (relwidth=0.45, height=20, relx=0.35, rely=.2)

L4 = tk.Label(root, borderwidth=2, relief='sunken', text="folder directory (OPTIONAL)")
L4.place(width=160, height=20, relx=0.08, rely=.25)
E4 = tk.Entry(root, bd =2)
E4.place (relwidth=0.45, height=20, relx=0.35, rely=.25)

L4b = tk.Label(root, text="")
L4b.place(relwidth=.4, height=20, relx=.38, rely=.45)
L4b.config(text='leaving folder directory empty will save to the current directory')

ImgScrape = tk.Button(root, text="S\nU\nB\nM\nI\nT",padx=10, pady=5, command=input_img_scrape)
ImgScrape.place(relwidth=0.04, relheight=0.185, relx=0.9, rely=.1)

ImgScrapeClr = tk.Button(root, text="C\nL\nE\nA\nR",padx=10, pady=5, command=clr_img_scrape)
ImgScrapeClr.place(relwidth=0.04, relheight=0.185, relx=0.85, rely=.1)

#TABLE SCRAPER BELOW ---------------------------------------------

TableLabel = tk.Label(root, text="DATATABLE SCRAPER")
TableLabel.place(width=145, height=20, relx=0.5, rely=.7)

L5 = tk.Label(root, borderwidth=2, relief='sunken', text="enter name for datatable")
L5.place(width=160, height=20, relx=0.08, rely=.75)
E5 = tk.Entry(root, bd =2)
E5.place (relwidth=0.45, height=20, relx=0.35, rely=.75)

L6 = tk.Label(root, borderwidth=2, relief='sunken', text="enter wikipedia url here")
L6.place(width=160, height=20, relx=0.08, rely=.8)
E6 = tk.Entry(root, bd =2)
E6.place (relwidth=0.45, height=20, relx=0.35, rely=.8)

L7 = tk.Label(root, borderwidth=2, relief='sunken', text="folder directory (OPTIONAL)")
L7.place(width=160, height=20, relx=0.08, rely=.85)
E7 = tk.Entry(root, bd =2)
E7.place (relwidth=0.45, height=20, relx=0.35, rely=.85)

var = tk.IntVar()
R1 = tk.Radiobutton(root, text="CSV", variable=var, value=0)
R1.place(relx=0.37, rely=.9)

R2 = tk.Radiobutton(root, text="JSON", variable=var, value=1)
R2.place(relx=0.55, rely=.9)

R3 = tk.Radiobutton(root, text="HTML", variable=var, value=2)
R3.place(relx=0.7, rely=.9)

TableScrape = tk.Button(root, text="S\nU\nB\nM\nI\nT",padx=10, pady=5, command=input_table_scrape)
TableScrape.place(relwidth=0.04, relheight=0.185, relx=0.9, rely=.73)

TableScrapeClr = tk.Button(root, text="C\nL\nE\nA\nR",padx=10, pady=5, command=clr_table_scrape)
TableScrapeClr.place(relwidth=0.04, relheight=0.185, relx=0.85, rely=.73)


#canvas.pack()
root.mainloop()